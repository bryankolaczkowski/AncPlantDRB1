#!/bin/bash

#PBS -N runASR_muscle
#PBS -o runASR_muscle.out
#PBS -j oe
#PBS -l nodes=1:ppn=4:infiniband
#PBS -l pmem=4800mb
#PBS -l walltime=12:00:00

cd $PBS_O_WORKDIR
T=$PBS_NUM_PPN
#T=4

module load raxml
base=aligned_muscle

# remove undetermined cols
./remove_undetermined.py ../${base}.fasta > ${base}.fasta

# make binary data
./make01.py ${base}.fasta > ${base}.01.fasta

# calculate ancestral protein sequences #
raxmlHPC-PTHREADS-SSE3 -T $T -f A -m PROTCATLGF -t ../RAxML_fastTree.${base}.shsupport.rooted -s ${base}.fasta -n ${base}.ancseqs

# calculate ancestral indels using binary-data model #
raxmlHPC-PTHREADS-SSE3 -T $T -f A -m BINCAT -t ../RAxML_fastTree.${base}.shsupport.rooted -s ${base}.01.fasta -n ${base}.ancindels

# combine ASR sequences and gaps #
./putIndels.py RAxML_marginalAncestralStates.${base}.ancseqs RAxML_marginalAncestralStates.${base}.ancindels > ${base}.mlasr.fasta

echo "done"
exit 0

