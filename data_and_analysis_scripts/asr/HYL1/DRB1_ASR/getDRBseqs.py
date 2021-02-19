#!/usr/bin/python

import sys

start_trim = 60
end_trim   = 300

N          = 0
ave_middle = 0
ave_tail   = 0

handle = open("unaligned.smallids.domains.csv","r")
handle.readline()
for line in handle:
	line = line.strip()
	linearr = line.split(",")
	gid = linearr[0]
	spp = linearr[1]
	seq = linearr[6]
	seqlen = len(seq)
	
	if linearr[4] or linearr[5]:
		continue
		
	dsrm1 = linearr[2]
	dsrm2 = linearr[3]
	b1 = int(dsrm1.split("..")[0])
	e1 = int(dsrm1.split("..")[1])
	b2 = int(dsrm2.split("..")[0])
	e2 = int(dsrm2.split("..")[1])
	
	#print "%d..%d S=%d" % (b1,e2,seqlen)
	
	if b1 <= start_trim and e2 >= seqlen-end_trim:
		N          += 1
		ave_middle += b2-e1
		ave_tail   += seqlen-e1
		sys.stdout.write(">%s_%s\n%s\n" % (gid,spp,seq))
handle.close()

#print "%f %f" % (ave_middle/float(N), ave_tail/float(N))

	
	