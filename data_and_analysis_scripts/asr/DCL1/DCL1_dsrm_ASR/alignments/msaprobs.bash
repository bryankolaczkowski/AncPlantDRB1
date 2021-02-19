#!/bin/bash

#PBS -N msaprobs
#PBS -o msaprobs.out
#PBS -j oe
#PBS -l nodes=1:ppn=8
#PBS -l pmem=22gb
#PBS -l walltime=72:00:00

# leave for qsub script          #
# comment out to run on dev node #
cd $PBS_O_WORKDIR

/home/bryank/gator/src/MSAProbs-0.9.7/MSAProbs/msaprobs -num_threads 8 ../sequence_data/unaligned.smallids.fasta > aligned_msaprobs.fasta

echo "done"
exit 0

