#!/usr/bin/python

import sys
import os
import glob

pkd_prediction_sh="""#!/bin/bash

module add openbabel
module add R

basedr=%s

for i in struct.[0-9].pdb;	do
	#extract protein and ligand
	${basedr}/extractChain.py $i A   > $i.protein.pdb
	${basedr}/extractChain.py $i B C > $i.ligand.pdb
	#convert ligand to mol2
	babel -ipdb $i.ligand.pdb -omol2 $i.ligand.mol2
	#creates shortcuts for the required files
	ln -s ${basedr}/glm/GLM-Score-master/asa ./
	ln -s ${basedr}/glm/GLM-Score-master/R ./
	ln -s ${basedr}/glm/GLM-Score-master/hydrophobicity.param ./
	ln -s ${basedr}/glm/GLM-Score-master/tension.param ./

	#predict pKd 
	${basedr}/glm/GLM-Score-master/GLM-Score $i.protein.pdb $i.ligand.pdb $i.ligand.mol2 protein
done
"""

batchscr="""#!/bin/bash

#SBATCH --job-name=pkd_%s
#SBATCH --output pkd_%s.out
#SBATCH --error pkd_%s.err
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=48:00:00
date;hostname;pwd

module load intel/2016.0.109

basedr=%s

for f in ${basedr}/%s/*/;
do
	if [ -a $f/struct_result.txt ] &&  [ `grep -c "predicted pKD:" $f/struct_result.txt` -gt 9 ] ; then
		echo "passed $f"
	else
		`rm $f/struct_result.txt`
		[ -d $f ] && cd "$f" && echo Entering into $f && ${basedr}/pkd_predictions.sh;
	fi
done;
"""

# write pkd_predictions.sh script #
outf = open("pkd_predictions.sh", "w")
outf.write(pkd_prediction_sh % os.getcwd())
outf.close()
os.system("chmod 755 pkd_predictions.sh")

# write and launch prediction scripts #
for d in glob.glob("D*"):
	outf = open("pkd_%s.bash" % d, "w")
	outf.write(batchscr % (d,d,d,os.getcwd(),d))
	outf.close()
	# launch #
	os.system("sbatch pkd_%s.bash" % d)

