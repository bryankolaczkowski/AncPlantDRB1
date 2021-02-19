#!/bin/bash

#PBS -N mafft
#PBS -o mafft.out
#PBS -j oe
#PBS -l nodes=1:ppn=1
#PBS -l pmem=16800mb
#PBS -l walltime=72:00:00

# leave for qsub script          #
# comment out to run on dev node #
cd $PBS_O_WORKDIR

module load mafft
mafft-einsi ../sequence_data/unaligned.smallids.fasta > aligned_mafft.fasta

echo "done"
exit 0

