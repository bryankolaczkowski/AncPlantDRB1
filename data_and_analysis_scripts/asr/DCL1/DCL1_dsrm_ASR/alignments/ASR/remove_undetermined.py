#!/usr/bin/python

import sys

# read in original sequence alignment #
ids  = []
seqs = []

handle = open(sys.argv[1], "r")
line = handle.readline()
while line:
	if line[0] == ">":
		id = line[1:].strip()
		seq = ""
		line = handle.readline()
		while line and line[0] != ">":
			seq += line.strip()
			line = handle.readline()
		ids.append(id)
		seqs.append(seq)
handle.close()

# remove completely undetermined columns #
undeter_cols = []
for i in range(len(seqs[0])):
	undet = True
	for j in range(len(ids)):
		if seqs[j][i] != "-" and seqs[j][i] != "X" and seqs[j][i] != "x":
			undet = False
	if undet:
		undeter_cols.append(i)

for i in range(len(ids)):
	id = ids[i]
	seq = seqs[i]
	newseq = ""
	for j in range(len(seq)):
		if j not in undeter_cols:	
			newseq += seq[j]
	sys.stdout.write(">%s\n%s\n" % (id,newseq))

