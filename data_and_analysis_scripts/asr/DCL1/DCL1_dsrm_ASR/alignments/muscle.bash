#!/bin/bash

#PBS -N muscle
#PBS -o muscle.out
#PBS -j oe
#PBS -l nodes=1:ppn=1
#PBS -l pmem=16800mb
#PBS -l walltime=72:00:00

# leave for qsub script          #
# comment out to run on dev node #
cd $PBS_O_WORKDIR

module load muscle
muscle -in ../sequence_data/unaligned.smallids.fasta -out aligned_muscle.fasta

echo "done"
exit 0

