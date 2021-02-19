#!/bin/bash

#SBATCH --job-name=rdinfo
#SBATCH --time=72:00:00
#SBATCH --mail-user=kaadland@ufl.edu
#SBATCH --mail-type=FAIL,END
#SBATCH --output=rdinfo.%a.out
#SBATCH --error=rdinfo.%a.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=100M
#SBATCH --array=0-8

#date;hostname;pwd

module load python3
module load mafft

plants=("COL" "HYL1" "ANCHYL1")
reps=(1 2 3)

rep=${reps[$SLURM_ARRAY_TASK_ID % 3]}
plant=${plants[($SLURM_ARRAY_TASK_ID / 3)]}

echo $rep $plant

./02_getReadEndInfo.py ${plant} ${rep} > ${plant}_${rep}.miRNAfidelity.csv

#date
echo $SLURM_ARRAY_TASK_ID done.

