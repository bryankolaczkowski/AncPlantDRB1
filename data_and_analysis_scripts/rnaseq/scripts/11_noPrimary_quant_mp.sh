#!/bin/bash

#SBATCH --job-name=noPrimary_mp
#SBATCH --time=10:00:00
#SBATCH --mail-user=kaadland@ufl.edu
#SBATCH --mail-type=FAIL,END
#SBATCH --output=noPrimary_mp.log
#SBATCH --error=noPrimary_mp.err
#SBATCH --nodes=1
#SBATCH --ntasks=1

module load salmon

#This value should be a negative (typically small) integer. It controls the score given to a mismatch in the alignment between the query (read) and the reference.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i At_noPrimary_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --mp=-2 -o mp_noPrimary_BKoptions_quants/${samp}_mp_noPrimary_BKoptions_quants
done
echo "ANCHYL1 salmon --mp noPrimary done"
