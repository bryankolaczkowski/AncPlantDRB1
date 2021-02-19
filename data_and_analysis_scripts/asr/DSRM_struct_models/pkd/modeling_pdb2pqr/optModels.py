#!/usr/bin/python

import sys
import os
import shutil
import glob

## set up directories and copy needed modeling files ##
## run structural models through pdb2pqr to optimze  ##

basedir = sys.argv[1]

for fname in glob.glob("%s/*.BESTMODEL_*.pdb" % basedir):
	thedir = fname.split("/")[0] + "/" + fname.split("/")[1]
	theid  = fname.split("/")[-1].split(".")[0]
	repnum = int(fname.split("/")[-1].split(".")[-2].split("_")[-1])
	
	newdirid = "%s_R%d" % (theid,repnum)
	workdir = "%s/%s" % (thedir,newdirid)

	if not os.path.exists(workdir):
		os.mkdir(workdir)
	
	shutil.copy(fname, "%s/prot_prot.pdb" % workdir)
	
	# better change into the workdir for the next part #
	workingdir = os.getcwd()
	os.chdir(workdir)

	#                               #
	# optimize the structural model #
	#                               #

	fbase = "prot_prot.pdb"
	# add hydrogens and optimize for hydrogen bonding #
	cmd = "pdb2pqr --ff amber --chain %s finalstructure.pdb" % fbase
	os.system(cmd)

	os.chdir(workingdir)

