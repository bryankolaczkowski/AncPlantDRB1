#!/bin/bash

#SBATCH --job-name=salmonVM_noPrimary_options
#SBATCH --time=48:00:00
#SBATCH --mail-user=kaadland@ufl.edu
#SBATCH --mail-type=FAIL,END
#SBATCH --output=salmonVM_noPrimary_options.log
#SBATCH --error=salmonVM_noPrimary_options.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=1KB

module load salmon

#Controls the minimum allowed score for a mapping to be considered valid.
#for fn in ../ANCHYL1_{1..3};
#do
#samp=`basename ${fn}`
#echo "processing sample ${samp}"
#salmon quant -i At_noPrimary_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --minScoreFraction 5 -o minScore_noPrimary_options_quants/${samp}_minScore_noPrimary_options_quants
#done
#echo "ANCHYL1 salmon --minScoreFraction noPrimary done"

#The range-factorization feature allows using a data-driven likelihood factorization, which can improve quantification accuracy on certain classes of “difficult” transcripts.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i At_noPrimary_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --rangeFactorizationBins 5 -o vm_noPrimary_options_quants/${samp}_vm_noPrimary_options_quants
done
echo "ANCHYL1 salmon --rangeFactorizationBins noPrimary done"


#This value should be a positive (typically small) integer. It controls the score given to a match in the alignment between the query (read) and the reference.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i At_noPrimary_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --ma 5 -o ma_noPrimary_options_quants/${samp}_ma_noPrimary_options_quants
done
echo "ANCHYL1 salmon --ma noPrimary done"


#This value should be a negative (typically small) integer. It controls the score given to a mismatch in the alignment between the query (read) and the reference.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i At_noPrimary_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --mp 5 -o mp_noPrimary_options_quants/${samp}_mp_noPrimary_options_quants
done
echo "ANCHYL1 salmon --mp noPrimary done"


#This value should be a positive (typically small) integer. It controls the score penalty attributed to an alignment for each new gap that is opened.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i At_noPrimary_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --go 5 -o go_noPrimary_options_quants/${samp}_go_noPrimary_options_quants
done
echo "ANCHYL1 salmon --go noPrimary done"


#This value should be a positive (typically small) integer. It controls the score penalty attributed to the extension of a gap in an alignment.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i At_noPrimary_index -l U -r ../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --ge 5 -o ge_noPrimary_options_quants/${samp}_ge_noPrimary_options_quants
done
echo "ANCHYL1 salmon --ge noPrimary done"

