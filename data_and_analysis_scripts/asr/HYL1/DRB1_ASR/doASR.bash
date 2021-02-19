#!/bin/bash

base=allDRBs.linsi.FORASR
raxml=~/Documents/software/standard-RAxML-master/raxmlHPC-AVX2
treef=allDRBs.linsi.FORASR.rooted.fasttree

# make binary data
./make01.py ${base}.fasta > ${base}.01.fasta

# calculate ancestral protein sequences #
${raxml} -f A -m PROTCATLGF -t ${treef} -s ${base}.fasta    -n ${base}.ancseqs
# calculate ancestral indels using binary-data model #
${raxml} -f A -m BINCAT     -t ${treef} -s ${base}.01.fasta -n ${base}.ancindels

# combine ASR sequences and gaps #
./putIndels.py RAxML_marginalAncestralStates.${base}.ancseqs RAxML_marginalAncestralStates.${base}.ancindels > ${base}.mlasr.fasta

