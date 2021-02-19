#!/usr/bin/env python

import sys

filename = sys.argv[1]

infile = open(filename, "r")

line = infile.readline()

for line in infile:
	line = line.rstrip("\n")
	mylist = line.strip().split()
	if "miRNA_primary_transcript" not in mylist:
		print line
infile.close()
