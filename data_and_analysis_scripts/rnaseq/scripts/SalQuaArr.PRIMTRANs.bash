#!/bin/bash

#SBATCH --job-name=SalQuaArr
#SBATCH --time=24:00:00
#SBATCH --mail-user=kaadland@ufl.edu
#SBATCH --mail-type=FAIL,END
#SBATCH --output=SalQuaArr.%a.Ar11.PRIMTRANS.out
#SBATCH --error=SalQuaArr.%a.Ar11.PRIMTRANS.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=10GB
#SBATCH --array=0-8

#date;hostname;pwd

module load salmon

libs=("Araport11.PRIMTRANS_plus_decoys.index")
plants=("COL" "HYL1" "ANCHYL1")
reps=(1 2 3)

rep=${reps[$SLURM_ARRAY_TASK_ID % 3]}
plant=${plants[($SLURM_ARRAY_TASK_ID / 3) % 3]}
lib=${libs[($SLURM_ARRAY_TASK_ID / 9) % 1]}

echo $rep $plant

salmon quant -p 8 -i ${lib} -l U -r ../fastq_files/${plant}_${rep}_cutadapt.fastq.gz --validateMappings --writeMappings=${plant}_${rep}_Ar11.PRIMTRANS_plus_decoys.mappedReads --minScoreFraction 0.8 --ma=1 --mp=-2 --go=5 --ge=1 -o ${plant}_${rep}_Ar11.PRIMTRANS_plus_decoys.quants

#date
echo $SLURM_ARRAY_TASK_ID done.
