#!/bin/bash

#SBATCH --job-name=SalQuaArr
#SBATCH --time=24:00:00
#SBATCH --mail-user=kaadland@ufl.edu
#SBATCH --mail-type=FAIL,END
#SBATCH --output=SalQuaArr.%a.out
#SBATCH --error=SalQuaArr.%a.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=10GB
#SBATCH --array=0-17

#date;hostname;pwd

module load salmon

libs=("At_miRNAonly_index" "At_noPrimary_index")
plants=("COL" "HYL1" "ANCHYL1")
reps=(1 2 3)

rep=${reps[$SLURM_ARRAY_TASK_ID % 3]}
plant=${plants[($SLURM_ARRAY_TASK_ID / 3) % 3]}
lib=${libs[($SLURM_ARRAY_TASK_ID / 9) % 2]}

echo $rep $plant $lib

salmon quant -p 8 -i ${lib} -l U -r ../fastq_files/${plant}_${rep}_cutadapt.fastq.gz --validateMappings --minScoreFraction 0.8 --ma=1 --mp=-2 --go=5 --ge=1 -o ${plant}_${rep}_${lib}_quants

#date
echo $SLURM_ARRAY_TASK_ID done.

