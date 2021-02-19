#!/usr/bin/python

import sys

handle = open("dsrm_structure_aln.fasta", "r")
line = handle.readline()
while line:
	if line[0] == ">":
		id = line.strip()
		se = ""
		line = handle.readline()
		while line and line[0] != ">":
			se += line.strip()
			line = handle.readline()
		sys.stdout.write("%s\n%s-----%s\n" % (id,se,se))
	else:
		line = handle.readline()
handle.close()
