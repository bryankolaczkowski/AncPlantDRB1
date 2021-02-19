#!/bin/bash

#SBATCH --job-name=pkd_D0
#SBATCH --output pkd_D0.out
#SBATCH --error pkd_D0.err
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=48:00:00
date;hostname;pwd

module load intel/2016.0.109

basedr=/ufrc/bryankol/kaadland/analyses/DSRM_struct_models/pkd/structures

for f in ${basedr}/D0/*/;
do
	if [ -a $f/struct_result.txt ] &&  [ `grep -c "predicted pKD:" $f/struct_result.txt` -gt 9 ] ; then
		echo "passed $f"
	else
		`rm $f/struct_result.txt`
		[ -d $f ] && cd "$f" && echo Entering into $f && ${basedr}/pkd_predictions.sh;
	fi
done;
