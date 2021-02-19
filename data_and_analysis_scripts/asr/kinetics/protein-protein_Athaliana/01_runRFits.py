#!/usr/bin/python

import glob
import os

for d in glob.glob("analyses/*/*/K*/rep*.data"):
	print d
	rcmd = "R --no-save --args %s < NonLinFit.R > %s.rout" % (d,d)
#	print rcmd
	os.system(rcmd)

