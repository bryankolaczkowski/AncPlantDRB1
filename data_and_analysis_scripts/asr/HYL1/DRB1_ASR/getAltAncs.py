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
ml_asrs   = {}
alt_res   = {}

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

handle = open("allDRBs.linsi.FORASR.mlasr.fasta", "r")
line = handle.readline()
while line:
	id = line.strip()[1:]
	se = handle.readline().strip()
	ml_asrs[id] = se
	line = handle.readline()
handle.close()

aa_codes = ["A","R","N","D","C","Q","E","G","H","I","L","K","M","F","P","S","T","W","Y","V"]

handle = open("RAxML_marginalAncestralProbabilities.allDRBs.linsi.FORASR.ancseqs", "r")
line = handle.readline()
while line:
	if line.strip() in key_nodes.keys():
		id = line.strip()
		maxprobs = []
		alts     = []
		altc     = 0
		while line and line != "\n":
			probs = line.split()
			max = 0.0
			for s in probs:
				if float(s) > max:
					max = float(s)
			alt = ""
			for i in range(len(probs)):
				x = float(probs[i])
				if x < max and x > ALT_CUTOFF:
					altc += 1
					alt   = aa_codes[i]
			maxprobs.append(max)
			alts.append(alt)
			line = handle.readline()
		seq_probs[id] = maxprobs
		num_altrs[id] = float(altc)
		alt_res[id]   = alts
	else:
		line = handle.readline()
handle.close()

for id in key_nodes.keys():
	ml_asr   = ml_asrs[id]
	gap_prob = gap_probs[id]
	alts     = alt_res[id]

	sys.stdout.write(">%s\n%s\n" % (key_nodes[id],ml_asr))
	
	sys.stdout.write(">%s_ALT\n" % key_nodes[id])
	
	for i in range(len(ml_asr)):
		if ml_asr[i] != "-" and gap_prob[i] > 0.4:
			sys.stdout.write("-")
		elif alts[i] != "":
			sys.stdout.write(alts[i])
		else:
			sys.stdout.write(ml_asr[i])
		
	sys.stdout.write("\n")

