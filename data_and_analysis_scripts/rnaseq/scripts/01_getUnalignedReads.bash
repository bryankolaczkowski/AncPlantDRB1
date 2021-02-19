#!/bin/bash

#SBATCH --job-name=gur
#SBATCH --output gur.out
#SBATCH --error gur.err
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1G
#SBATCH --time=6:00:00
#SBATCH --qos=bryankol-b
date;hostname;pwd

module load python3

./01_getUnalignedReads.py

date
echo "done."

