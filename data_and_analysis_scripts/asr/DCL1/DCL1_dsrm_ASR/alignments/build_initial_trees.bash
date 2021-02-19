#!/bin/bash

#PBS -N tree
#PBS -o tree.out
#PBS -j oe
#PBS -l nodes=1:ppn=1
#PBS -l pmem=3800mb
#PBS -l walltime=16:00:00

# leave for qsub script          #
# comment out to run on dev node #
cd $PBS_O_WORKDIR

module load fasttree

#FastTree aligned_mafft.fasta     > aligned_mafft.tre
#FastTree aligned_muscle.fasta    > aligned_muscle.tre
#FastTree aligned_msaprobs.fasta  > aligned_msaprobs.tre
FastTree aligned_probcons.fasta  > aligned_probcons.tre
#FastTree aligned_probalign.fasta > aligned_probalign.tre

echo "done"
exit 0

