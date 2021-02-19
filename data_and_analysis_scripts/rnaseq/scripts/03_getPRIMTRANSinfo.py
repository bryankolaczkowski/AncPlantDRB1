#!/usr/bin/env python3

import sys
import os

# read miRNAs in FASTA #
mirna_fasta = {}
handle = open("/home/bryank/gator2/analyses/Araport11_transcriptome/PRIM_TRANS/Araport11.miRNAs_for_primtrans.fasta", "r")
line = handle.readline()
while line:
	if line[0] == ">":
		id = line[1:].strip()
		se = handle.readline().strip()[6:-6] # we'll trim the first and last few NTs for matching #
		mirna_fasta[id] = se
	line = handle.readline()
handle.close()

# read which miRNAs map to each primary_transcript #
pt_to_mir = {}
handle = open("/ufrc/bryankol/bryank/analyses/Araport11_transcriptome/PRIM_TRANS/PRIMTRANS_to_miRNA.ids", "r")
for line in handle:
	linearr = line.split()
	pt_to_mir[linearr[0]] = linearr[1:]
handle.close()

# main stuf... #
basedir    = "/ufrc/bryankol/kaadland/drb1_RNASeq/salmon"
treatments = ["ANCHYL1", "HYL1", "COL"]
reps       = [1, 2, 3]
extension  = "_Ar11.PRIMTRANS_plus_decoys.mappedReads"
idprefix   = "PRIMTRANS_"

if len(sys.argv) == 3:
	treatments = [     sys.argv[1]  ]
	reps       = [ int(sys.argv[2]) ]

sys.stdout.write("treatment,rep,primary_transcript,total_reads,non_miRNA_reads\n")

for rep in reps:
	for treatment in treatments:

		# read the reads mapping to each primary transcript #
		primtrans_counts = {}

		readfname = "%s/%s_%d%s" % (basedir, treatment, rep, extension)
		handle = open(readfname, "r")
		for line in handle:
			linearr = line.split()
			if len(linearr) == 14:
				ID   = linearr[2]
				rdSE = linearr[9][:-4]
				if ID.find(idprefix) == 0:
					if ID not in primtrans_counts.keys():
						primtrans_counts[ID] = [0,0]
					# now parse the read! #
					primtrans_counts[ID][0] += 1	# read maps to primary transcript #
					# check if read is miRNA #
					read_is_miRNA = False
					if ID in pt_to_mir.keys():
						for mirnaseq in mirna_fasta.values():
							if rdSE.find(mirnaseq) != -1 and len(rdSE) <= len(mirnaseq)+28:
								read_is_miRNA = True
								break
					if not read_is_miRNA:
						primtrans_counts[ID][1] += 1
		handle.close()

		for (id, counts) in primtrans_counts.items():
			sys.stdout.write("%s,%d,%s,%d,%d\n" % (treatment, rep, id, counts[0], counts[1]))

