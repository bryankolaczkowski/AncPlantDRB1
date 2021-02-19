#!/bin/bash

#SBATCH --job-name=salmonVM_options
#SBATCH --time=48:00:00
#SBATCH --mail-user=kaadland@ufl.edu
#SBATCH --mail-type=FAIL,END
#SBATCH --output=salmonVM_options.log
#SBATCH --error=salmonVM_options.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=5MB

module load salmon

#Controls the minimum allowed score for a mapping to be considered valid.
#for fn in ../ANCHYL1_{1..3};
#do
#samp=`basename ${fn}`
#echo "processing sample ${samp}"
#salmon quant -i mature_miRNA_index -l U -r ../../../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --minScoreFraction 5 -o minScore_quants/${samp}_minScore_quant
#done
#echo "ANCHYL1 salmon --minScoreFraction done"

#The range-factorization feature allows using a data-driven likelihood factorization, which can improve quantification accuracy on certain classes of “difficult” transcripts.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i mature_miRNA_index -l U -r ../../../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --rangeFactorizationBins 5 -o rangeFact_quants/${samp}_rangeFact_quant
done
echo "ANCHYL1 salmon --rangeFactorizationBins done"


#This value should be a positive (typically small) integer. It controls the score given to a match in the alignment between the query (read) and the reference.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i mature_miRNA_index -l U -r ../../../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --ma 5 -o ma_quants/${samp}_ma_quant
done
echo "ANCHYL1 salmon --ma done"


#This value should be a negative (typically small) integer. It controls the score given to a mismatch in the alignment between the query (read) and the reference.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i mature_miRNA_index -l U -r ../../../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --mp 5 -o mp_quants/${samp}_mp_quant
done
echo "ANCHYL1 salmon --mp done"


#This value should be a positive (typically small) integer. It controls the score penalty attributed to an alignment for each new gap that is opened.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i mature_miRNA_index -l U -r ../../../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --go 5 -o go_quants/${samp}_go_quant
done
echo "ANCHYL1 salmon --go done"


#This value should be a positive (typically small) integer. It controls the score penalty attributed to the extension of a gap in an alignment.
for fn in ../ANCHYL1_{1..3};
do
samp=`basename ${fn}`
echo "processing sample ${samp}"
salmon quant -i mature_miRNA_index -l U -r ../../../fastq_files/${samp}_cutadapt.fastq.gz --validateMappings --ge 5 -o ge_quants/${samp}_ge_quant
done
echo "ANCHYL1 salmon --ge done"
