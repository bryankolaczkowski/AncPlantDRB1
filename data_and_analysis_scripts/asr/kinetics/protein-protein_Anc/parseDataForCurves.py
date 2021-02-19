#!/usr/bin/python

import sys
import os
import glob

for f in glob.glob("analyses/DCL1_dsrm*/*/Kd/rep1.data"):
	name = f.split("/")[1] + "_" + f.split("/")[2]
	
	conc = []
	kd1  = []
	km1  = []
	kd2  = []
	km2  = []
	
	handle = open(f, "r")
	for line in handle:
		conc.append(line.split()[0])
		kd1.append(line.split()[1])
	handle.close()
		
	fname = f.replace("Kd","Km")
	handle = open(fname, "r")
	for line in handle:
		km1.append(line.split()[1])
	handle.close()
	
	fname = f.replace("rep1","rep2")
	handle = open(fname, "r")
	for line in handle:
		kd2.append(line.split()[1])
	handle.close()
	
	fname = f.replace("rep1","rep2").replace("Kd","Km")
	handle = open(fname, "r")
	for line in handle:
		km2.append(line.split()[1])
	handle.close()
	
	print name
	for i in range(len(conc)):
		print "%s\t%s\t%s\t%s\t%s" % (conc[i], kd1[i], km1[i], kd2[i], km2[i])
		
	sys.stdout.write("\n")
	