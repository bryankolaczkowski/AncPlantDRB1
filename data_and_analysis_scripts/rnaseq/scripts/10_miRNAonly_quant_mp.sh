#!/bin/bash

#SBATCH --job-name=miRNAonly_mp
#SBATCH --time=48:00:00
#SBATCH --mail-user=kaadland@ufl.edu
#SBATCH --mail-type=FAIL,END
#SBATCH --output=miRNAonly_mp.log
#SBATCH --error=miRNAonly_mp.err
#SBATCH --nodes=1
#SBATCH --ntasks=1

module load salmon

#This value should be a negative (typically small) integer. It controls the score given to a mismatch in the alignment between the query (read) and the reference.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i At_miRNAonly_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --mp=-2 -o mp_miRNAonly_BKoptions_quants/${samp}_mp_miRNAonly_BKoptions_quants
done
time
echo "ANCHYL1 salmon --mp miRNAonly done"
