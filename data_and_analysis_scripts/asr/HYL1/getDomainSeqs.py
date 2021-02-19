#!/usr/bin/python

import sys

want_domain  = "DSRM"
domain_count = 2

PLUS_MINUS_RES = 10
MIN_DOM_LEN    = 65
MAX_DOM_LEN    = 110
	
base    = "unaligned.smallids"
infname = base + ".domains.csv"
handle  = open(infname, "r")

header_arr = handle.readline().strip().split(",")[2:-1]
want_cols  = [2,3]

outfiles = []
taxfiles = []
for i in range(len(want_cols)):
	outfiles.append(open("%s.%s%d.fasta" % (base,want_domain,i+1), "w"))
	taxfiles.append(open("%s.%s%d.taxa"  % (base,want_domain,i+1), "w"))

for line in handle:
	linearr = line.strip().split(",")
	gid     = linearr[0]
	spp     = linearr[1]
	seq     = linearr[-1]
	id      = gid + "_" + spp
	doms    = []
	for n in range(len(want_cols)):
		i       = want_cols[n]
		outf    = outfiles[n]
		taxf    = taxfiles[n]
		beg_end = linearr[i]
		if beg_end:
			beg_end_arr = beg_end.split("..")
			beg = int(beg_end_arr[0]) - PLUS_MINUS_RES - 1
			if beg < 0:
				beg = 0
			end = int(beg_end_arr[1]) + PLUS_MINUS_RES
			domseq = seq[beg:end]
			if len(domseq) >= MIN_DOM_LEN and len(domseq) <= MAX_DOM_LEN:
				outf.write(">%s\n%s\n" % (id, domseq))
				taxf.write("%s\n" % id)

handle.close()
for outf in outfiles:
	outf.close()
for taxf in taxfiles:
	taxf.close()

