#!/bin/bash

#SBATCH --job-name=trans_opt_quant
#SBATCH --time=96:00:00
#SBATCH --mail-user=kaadland@ufl.edu
#SBATCH --mail-type=FAIL,END
#SBATCH --output=trans_opt_quant.log
#SBATCH --error=trans_opt_quant.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=5GB

module load salmon

for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i ../reference_files/transcriptome_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --minScoreFraction 0.8 --ma=1 --mp=-2 --go=5 --ge=1 -o trans_quants/${samp}_trans_quant
done
echo "ANCHYL1 salmon transcriptome with options done"


#for fn in COL_{1..3};
#do
#samp=`basename ${fn}`
#echo "processing sample ${samp}"
#salmon quant -i index_At -l A -r ../fastq_files/${samp}_cutadapt.fastq.gz -p 8 -o quants/${samp}_quant
#done
#echo "COL salmon done"


#for fn in HYL1_{1..3};
#do
#samp=`basename ${fn}`
#echo "processing sample ${samp}"
#salmon quant -i index_At -l A -r ../fastq_files/${samp}_cutadapt.fastq.gz -p 8 -o quants/${samp}_quant
#echo "HYL1 salmon done"

#done
