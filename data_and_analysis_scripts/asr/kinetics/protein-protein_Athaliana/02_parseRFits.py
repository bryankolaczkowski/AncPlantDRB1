#!/usr/bin/python

import glob
import sys

for protdir in glob.glob("analyses/*"):
	protein = protdir.split("/")[-1]
	for rnadir in glob.glob("%s/*" % protdir):
		rnatype = rnadir.split("/")[-1]
		for measuredir in glob.glob("%s/K*" % rnadir):
			measuretype = measuredir.split("/")[-1]
			vals = []
			for infile in glob.glob("%s/rep*.data.rout" % measuredir):
				handle = open(infile, "r")
				line = handle.readline()
				while line and line.find("coef(summary(fit))") < 0:
					line = handle.readline()
				handle.readline()
				handle.readline()
				k = handle.readline().split()
				if len(k) > 1:
					vals.append(k[1])
				handle.close()
			sys.stdout.write("%s\t%s\t%s" % (protein,rnatype,measuretype))
			for v in vals:
				sys.stdout.write("\t%s" % v)
			sys.stdout.write("\n")

