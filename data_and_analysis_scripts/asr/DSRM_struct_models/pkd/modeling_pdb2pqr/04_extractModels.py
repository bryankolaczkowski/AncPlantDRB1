#!/usr/bin/python

import sys
import glob
import os

if len(sys.argv) > 1:
	sys.stderr.write("usage: 03_extractModels.py\n")
	sys.stderr.write(" This will extract the final optimized structure\n")
	sys.stderr.write(" as a pdb file (excluding solvent) and copy it to\n")
	sys.stderr.write(" ../structures/.\n")
	sys.exit(1)

for f in glob.glob("models/D*/*_R[0-9]/finalstructure.pdb"):
	farray = f.split("/")
	dir1 = farray[1]
	name = farray[2][:-3]
	rep  = farray[2][-1]

	# create directories if needed #
	outfname = "../structures/%s/%s" % (dir1,name)
	if not os.path.exists(outfname):
		os.makedirs(outfname)
	outfname += "/struct." + rep + ".pdb"
	
	# copy structure file #
	os.system("cp %s %s" % (f,outfname))
	print "done %s" % outfname

