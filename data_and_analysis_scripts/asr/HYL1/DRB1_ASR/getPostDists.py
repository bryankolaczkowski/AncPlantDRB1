#!/usr/bin/python

import os
import sys

ALT_CUTOFF = 0.3

key_nodes = {
"1417" : "ancDRB",
"1578" : "ancDRB1DRB6",
"1579" : "ancDRB1",
"1580" : "ancFlowering",
"1581" : "ancDicotMonocot",
"1582" : "ancDicot"
}

gap_probs = {}
seq_probs = {}
num_altrs = {}

handle = open("RAxML_marginalAncestralProbabilities.allDRBs.linsi.FORASR.ancindels", "r")
line = handle.readline()
while line:
	if line.strip() in key_nodes.keys():
		id = line.strip()
		probs = []
		line = handle.readline()
		while line and line != "\n":
			pgap = float(line.split()[0])
			probs.append(pgap)
			line = handle.readline()
		gap_probs[id] = probs
	else:
		line = handle.readline()
handle.close()

handle = open("RAxML_marginalAncestralProbabilities.allDRBs.linsi.FORASR.ancseqs", "r")
line = handle.readline()
while line:
	if line.strip() in key_nodes.keys():
		id = line.strip()
		maxprobs = []
		altc     = 0
		while line and line != "\n":
			probs = line.split()
			max = 0.0
			for s in probs:
				if float(s) > max:
					max = float(s)
			for s in probs:
				x = float(s)
				if x < max and x > ALT_CUTOFF:
					altc += 1
			maxprobs.append(max)
			line = handle.readline()
		seq_probs[id] = maxprobs
		num_altrs[id] = float(altc)
	else:
		line = handle.readline()
handle.close()

distcutoffs = [0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0]

for id in key_nodes.keys():
	counts = []
	for x in distcutoffs:
		counts.append(0.0)
	seqlen = len(gap_probs[id])
	for i in range(seqlen):
		if gap_probs[id][i] > 0.5:
			for j in range(len(distcutoffs)):
				if gap_probs[id][i] <= distcutoffs[j]:
					counts[j] += 1.0
					break
		else:
			for j in range(len(distcutoffs)):
				if seq_probs[id][i] <= distcutoffs[j]:
					counts[j] += 1.0
					break
	sys.stdout.write("%s\n" % key_nodes[id])
	for i in range(len(distcutoffs)):
		sys.stdout.write("%f\t%f\n" % (distcutoffs[i], (counts[i]/float(seqlen))))
	sys.stdout.write("alts:\t%f\n\n" % (num_altrs[id]/float(seqlen)))
	
