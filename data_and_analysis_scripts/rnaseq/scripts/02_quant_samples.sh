#!/bin/bash

#SBATCH --job-name=salmonVM
#SBATCH --time=15:00:00
#SBATCH --mail-user=kaadland@ufl.edu
#SBATCH --mail-type=FAIL,END
#SBATCH --output=salmonVM.log
#SBATCH --error=salmonVM.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=5GB

module load salmon

for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i mature_miRNA_index -l U -r ../../../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings -o vm_quants/${samp}_vm_quant
done
echo "ANCHYL1 salmon done"


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
