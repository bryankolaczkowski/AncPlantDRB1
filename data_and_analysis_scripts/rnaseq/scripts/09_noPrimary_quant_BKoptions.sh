#!/bin/bash

#SBATCH --job-name=salmonVM_noPrimary_BKoptions
#SBATCH --time=80:00:00
#SBATCH --mail-user=kaadland@ufl.edu
#SBATCH --mail-type=FAIL,END
#SBATCH --output=salmonVM_noPrimary_BKoptions.log
#SBATCH --error=salmonVM_noPrimary_BKoptions.err
#SBATCH --nodes=1
#SBATCH --ntasks=1

module load salmon

#Controls the minimum allowed score for a mapping to be considered valid.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i At_noPrimary_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --minScoreFraction 0.8 -o minScore_noPrimary_BKoptions_quants/${samp}_minScore_noPrimary_BKoptions_quants
done
echo "ANCHYL1 salmon --minScoreFraction noPrimary done"


#This value should be a positive (typically small) integer. It controls the score given to a match in the alignment between the query (read) and the reference.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i At_noPrimary_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --ma=1 -o ma_noPrimary_BKoptions_quants/${samp}_ma_noPrimary_BKoptions_quants
done
echo "ANCHYL1 salmon --ma noPrimary done"


#This value should be a negative (typically small) integer. It controls the score given to a mismatch in the alignment between the query (read) and the reference.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i At_noPrimary_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --mp=-2 -o mp_noPrimary_BKoptions_quants/${samp}_mp_noPrimary_BKoptions_quants
done
echo "ANCHYL1 salmon --mp noPrimary done"


#This value should be a positive (typically small) integer. It controls the score penalty attributed to an alignment for each new gap that is opened.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i At_noPrimary_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --go=5 -o go_noPrimary_BKoptions_quants/${samp}_go_noPrimary_BKoptions_quants
done
echo "ANCHYL1 salmon --go noPrimary done"


#This value should be a positive (typically small) integer. It controls the score penalty attributed to the extension of a gap in an alignment.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i At_noPrimary_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --ge=1 -o ge_noPrimary_BKoptions_quants/${samp}_ge_noPrimary_BKoptions_quants
done
echo "ANCHYL1 salmon --ge noPrimary done"
