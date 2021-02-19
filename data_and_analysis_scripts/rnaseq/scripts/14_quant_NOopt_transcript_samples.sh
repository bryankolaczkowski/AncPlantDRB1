#!/bin/bash

#SBATCH --job-name=trans_quant
#SBATCH --time=96:00:00
#SBATCH --mail-user=kaadland@ufl.edu
#SBATCH --mail-type=FAIL,END
#SBATCH --output=trans_8thread_quant.log
#SBATCH --error=trans_8thread_quant.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=1GB

module load salmon

for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i ../reference_files/transcriptome_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings -p 8 -o trans_8thread_quants/${samp}_trans_8threads_quant
done
echo "ANCHYL salmon transcriptome quantification  done"


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
