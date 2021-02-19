#!/usr/bin/python

import sys
import os
import glob

scriptstr="""#!/bin/bash

#SBATCH --job-name=pqr%s
#SBATCH --output pqr_%s.out
#SBATCH --error pqr_%s.err
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=11:00:00
#SBATCH --qos=bryankol-b
date;hostname;pwd

module load pdb2pqr/2.1.0

d=models/%s
./optModels.py $d

date
"""

if len(sys.argv) > 1:
	sys.stderr.write("usage: 02_optimizeStructureModels.py\n")
	sys.stderr.write(" This will optimize the structural models using pdb2pqr\n")
	sys.exit(1)

for topdir in glob.glob("models/D*"):
	thedir = topdir.split("/")[-1]
	outf = open("pqr_%s.bash" % thedir, "w")
	outf.write(scriptstr % (thedir,thedir,thedir,thedir))
	outf.close()
	os.system("sbatch pqr_%s.bash" % thedir)


