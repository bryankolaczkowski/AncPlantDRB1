#!/usr/bin/python

import sys


for d in ["DSRM1","DSRM2"]:
	taxa_to_keep = []
	handle = open("%s/contree.taxa" % d, "r")
	for line in handle:
		taxa_to_keep.append(line.strip())
	handle.close()
	
	outf   = open("%s/unaligned.trimmed.fasta" % d, "w")
	handle = open("%s/unaligned.fasta" % d, "r")
	line = handle.readline()
	while line:
		if line[0] == ">":
			id = line[1:].strip()
			se = ""
			line = handle.readline()
			while line and line[0] != ">":
				se += line.strip()
				line = handle.readline()
			if id in taxa_to_keep:
				outf.write(">%s\n%s\n" % (id,se))
		else:
			line = handle.readline()
	handle.close()
	outf.close()
