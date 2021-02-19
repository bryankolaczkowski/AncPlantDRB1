#!/bin/bash

#SBATCH --job-name=miRNAonly_ALLoptions
#SBATCH --time=96:00:00
#SBATCH --mail-user=kaadland@ufl.edu
#SBATCH --mail-type=FAIL,END
#SBATCH --output=miRNAonly_ALLoptions.log
#SBATCH --error=miRNAonly_ALLoptions.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=1KB

module load salmon

for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i At_miRNAonly_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --minScoreFraction 0.8 --ma=1 --mp=-2 --go=5 --ge=1 -o miRNAonly_ALLoptions_quants/${samp}_miRNAonly_ALLoptions_quants
done
echo "ANCHYL1 salmon miRNAonly ALL OPTIONS done"
date 
