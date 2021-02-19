#!/usr/bin/env python3

import sys
import os

# read miRNAs in FASTA #
mirna_fasta = {}
handle = open("/home/bryank/gator2/analyses/Araport11_transcriptome/PRIM_TRANS/Araport11.all_miRNAs.fasta", "r")
line = handle.readline()
while line:
	if line[0] == ">":
		id = line[1:].strip()
		se = handle.readline().strip()
		mirna_fasta[id] = se
	line = handle.readline()
handle.close()

basedir    = "/ufrc/bryankol/kaadland/drb1_RNASeq/salmon"
treatments = ["ANCHYL1", "HYL1", "COL"]
nreps      = 3
extension  = "mappedReads.miRNAs"

for rep in range(1,nreps+1):
	for treatment in treatments:
		# create output directory #
		outdir1 = "%s_%d" % (treatment,rep)
		if not os.path.exists(outdir1):
			os.mkdir(outdir1)

		# read the reads mapping to each miRNA #
		mirna_to_reads = {}
		readfname = "%s/%s.%s" % (basedir, outdir1, extension)
		handle = open(readfname, "r")
		for line in handle:
			linearr = line.split()
			if len(linearr) == 14:
				mrID = linearr[2]
				rdSE = linearr[9][:-4]
				if mrID in mirna_to_reads.keys():
					mirna_to_reads[mrID].append(rdSE)
				else:
					mirna_to_reads[mrID] = [rdSE]
		handle.close()

		# output unaligned reads in FASTA #
		for (realmir, realseq) in mirna_fasta.items():
			if realmir not in mirna_to_reads.keys():
				continue
			readarr = mirna_to_reads[realmir]
			if len(readarr) > 10:  # arbitrary read cutoff! #
				outdir = "%s/%s" % (outdir1, realmir)
				if not os.path.exists(outdir):
					os.mkdir(outdir)
				outf = open("%s/unaligned.fasta" % outdir, "w")
				outf.write(">%s\n%s\n" % (realmir,realseq))
				readnum = 0
				for read in readarr:
						outf.write(">R%d\n%s\n" % (readnum, read))
						readnum += 1
				outf.close()

