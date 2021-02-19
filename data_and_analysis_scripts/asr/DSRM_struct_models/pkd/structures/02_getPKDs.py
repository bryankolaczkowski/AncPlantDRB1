#!/usr/bin/python

import sys
import glob

outf = open("all_pkds.txt", "w")

for f in glob.glob("D*/*/struct_result.txt"):
	seqid = f.split("/")[1]
	pkds = []
	handle = open(f,"r")
	for line in handle:
		linearr = line.split()
		if linearr[0] == "predicted" and linearr[1] == "pKD:":
			pkds.append(float(linearr[2]))
	handle.close()
	pkds.sort(reverse=True)
	outf.write(seqid)
	for k in pkds:
		outf.write("\t%f" % k)
	outf.write("\n")

outf.close()

