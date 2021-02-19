#!/bin/bash

#PBS -N runRAxML_muscle
#PBS -o runRAxML_muscle.out
#PBS -j oe
#PBS -l nodes=1:ppn=4:infiniband
#PBS -l pmem=4800mb
#PBS -l walltime=72:00:00

cd $PBS_O_WORKDIR
T=$PBS_NUM_PPN
#T=4

module load raxml
base=aligned_muscle
# initial RAxML tree search;      #
# start from the FastTree ML tree #
raxmlHPC-PTHREADS-SSE3 -T $T -f T -p 218832 -m PROTCATLGF -t ${base}.tre -s ${base}.fasta -n ${base}.raxml

# calculate SH-like support under RAxML; #
# this will optimize the tree by NNI     #
raxmlHPC-PTHREADS-SSE3 -T $T -f J -p 109925 -m PROTCATLGF -t RAxML_bestTree.${base}.raxml -s ${base}.fasta -n ${base}.shsupport

echo "done"
exit 0

