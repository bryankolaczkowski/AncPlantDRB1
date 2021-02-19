#!/bin/bash

#PBS -N probalign
#PBS -o probalign.out
#PBS -j oe
#PBS -l nodes=1:ppn=1
#PBS -l pmem=28gb
#PBS -l walltime=96:00:00

# leave for qsub script          #
# comment out to run on dev node #
cd $PBS_O_WORKDIR

module load probalign

probalign ../sequence_data/unaligned.smallids.fasta > aligned_probalign.fasta

echo "done"
exit 0

