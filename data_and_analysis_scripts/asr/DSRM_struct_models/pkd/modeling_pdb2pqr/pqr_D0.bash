#!/bin/bash

#SBATCH --job-name=pqrD0
#SBATCH --output pqr_D0.out
#SBATCH --error pqr_D0.err
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=11:00:00
#SBATCH --qos=bryankol-b
date;hostname;pwd

module load pdb2pqr/2.1.0

d=models/D0
./optModels.py $d

date
