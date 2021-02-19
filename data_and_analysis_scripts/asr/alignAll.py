#!/usr/bin/python

import sys
import os

for d1 in ["DCL1","HYL1"]:
	for d2 in ["DSRM1","DSRM2"]:
		cmd = "ginsi --add %s/%s/unaligned.trimmed.fasta dsrm_structure_aln.fasta > %s/%s/ginsi.raw.fasta" % (d1,d2,d1,d2)
		os.system(cmd)
		