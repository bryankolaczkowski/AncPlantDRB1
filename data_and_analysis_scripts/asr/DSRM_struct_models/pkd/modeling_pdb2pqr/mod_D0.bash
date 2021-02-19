#!/bin/bash

#SBATCH --job-name=mod_D0
#SBATCH --output mod_D0.out
#SBATCH --error mod_D0.err
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=72:00:00
#SBATCH --qos=bryankol-b
date;hostname;pwd

cwd=`pwd`

module load  modeller/9.14

for d in `ls -d models/D0/*/`
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
