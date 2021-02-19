#!/bin/bash

#PBS -N pcons
#PBS -o pcons.out
#PBS -j oe
#PBS -l nodes=1:ppn=1
#PBS -l pmem=22gb
#PBS -l walltime=180:00:00

# leave for qsub script          #
# comment out to run on dev node #
cd $PBS_O_WORKDIR

/home/bryank/gator/src/probcons/probcons ../sequence_data/unaligned.smallids.fasta > aligned_probcons.fasta

echo "done"
exit 0

