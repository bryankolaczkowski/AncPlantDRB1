#!/usr/bin/python

import sys

mafftout     = open("asr_mafft.fasta", "w")
msaprobsout  = open("asr_msaprobs.fasta", "w")
muscleout    = open("asr_muscle.fasta", "w")
probalignout = open("asr_probalign.fasta", "w")
probconsout  = open("asr_probcons.fasta", "w")

def parseSeq(newid, oldid, alnname, outf):
	alnfname = "alignments/ASR/aligned_%s.fasta" % alnname
	seq = ""
	handle = open(alnfname,"r")
	line = handle.readline()
	while line:
		if line.find(oldid) > -1:
			seq = handle.readline().strip()
			break
		else:
			line = handle.readline()
	outf.write(">%s\n%s\n" % (newid,seq))

handle = open("AncSeqMap.txt", "r")
for line in handle:
	# parse ancestral sequences #
	if line.find("anc") == 0:
		linearr   = line.split()
		myid      = linearr[0]
		mafft     = linearr[1]
		msaprobs  = linearr[2]
		muscle    = linearr[3]
		probalign = linearr[4]
		probcons  = linearr[5]
		parseSeq(myid+"_mafft",mafft,"mafft.mlasr",mafftout)
		parseSeq(myid+"_msaprobs",msaprobs,"msaprobs.mlasr",msaprobsout)
		parseSeq(myid+"_muscle",muscle,"muscle.mlasr",muscleout)
		parseSeq(myid+"_probalign",probalign,"probalign.mlasr",probalignout)
		parseSeq(myid+"_probcons",probcons,"probcons.mlasr",probconsout)
		
	# parse A thaliana sequences #
	elif line.find("DCL") == 0:
		linearr = line.split()
		myid    = linearr[0]
		gid     = linearr[1]
		parseSeq(myid+"_At_mafft",gid,"mafft",mafftout)
		parseSeq(myid+"_At_msaprobs",gid,"msaprobs",msaprobsout)
		parseSeq(myid+"_At_muscle",gid,"muscle",muscleout)
		parseSeq(myid+"_At_probalign",gid,"probalign",probalignout)
		parseSeq(myid+"_At_probcons",gid,"probcons",probconsout)

handle.close()

mafftout.close()
msaprobsout.close()
muscleout.close()
probalignout.close()
probconsout.close()