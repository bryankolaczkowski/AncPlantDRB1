#!/usr/bin/python

import sys
import os
import glob

scriptstr="""#!/bin/bash

#SBATCH --job-name=mod_%s
#SBATCH --output mod_%s.out
#SBATCH --error mod_%s.err
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=72:00:00
#SBATCH --qos=bryankol-b
date;hostname;pwd

cwd=`pwd`

module load  modeller/9.14

for d in `ls -d models/%s/*/`
do
	v=${d:0:${#d}-1}
	if [ ! -f "${v}.BESTMODEL_9.pdb" ]
	then
		cd ${v}
		python ./runModeller.py > SCORES.txt
		python ./parseBestModel.py SCORES.txt
		cd ${cwd}
	fi
done

date
"""

if len(sys.argv) > 1:
	sys.stderr.write("usage: 02_launchStructures.py\n")
	sys.stderr.write(" This will launch the structural modeling step\n")
	sys.exit(1)

for d in glob.glob("models/D*"):
	d_name = d.split("/")[-1]
	outf = open("mod_%s.bash" % d_name, "w")
	outf.write(scriptstr % (d_name,d_name,d_name,d_name))
	outf.close()
	os.system("sbatch mod_%s.bash" % d_name)
	sys.stdout.write("done %s\n" % d_name)

sys.stdout.write("done.\n")

