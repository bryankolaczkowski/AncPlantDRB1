#!/usr/bin/python

import sys

SEQF = sys.argv[1]
INDF = sys.argv[2]

ancseqs = {}

handle = open(SEQF,"r")
for line in handle:
	linearr = line.split()
	id = linearr[0]
	seq = linearr[1]
	ancseqs[id] = seq
handle.close()

handle = open(INDF,"r")
for line in handle:
	linearr = line.split()
	id = linearr[0]
	ins = linearr[1]
	seq = ancseqs[id]

	sys.stdout.write(">%s\n" % id)
	for i in range(len(seq)):
		if ins[i] == "0" or seq[i] == "?":
			sys.stdout.write("-")
		else:
			sys.stdout.write(seq[i])
	sys.stdout.write("\n")

handle.close()

