#!/usr/bin/env python3

import sys
import matplotlib.pyplot

seqlen = -1
dsrm1  = [-1,-1]
dsrm2  = [-1,-1]
insertions = []
consmuts   = []
radmuts    = []

with open('differences_raw.txt', 'r') as handle:
  for line in handle:
    linearr = line.split()
    key = linearr[0]
    if key == 'len':
      seqlen = int(linearr[1])
    elif key == 'DSRM1':
      dsrm1 = [int(linearr[1]), int(linearr[2])]
    elif key == 'DSRM2':
      dsrm2 = [int(linearr[1]), int(linearr[2])]
    elif key == 'ins':
      insertions.append([int(linearr[1]), int(linearr[2])])
    else:
      pos = int(linearr[0])
      mut = int(linearr[1])
      if mut == 1:
        consmuts.append(pos)
      else:
        radmuts.append(pos)

#print(seqlen)
#print(dsrm1)
#print(dsrm2)
#print(insertions)
#print(consmuts)
#print(radmuts)

fig,ax = matplotlib.pyplot.subplots(figsize=(6.5,0.5))
ax.axis('off')

ax.axhline(color='gray',linewidth=0.5)
ax.scatter(consmuts, [-1]*len(consmuts), marker='^', s=6)
ax.scatter(radmuts,  [ 1]*len(radmuts),  marker='v', s=6)

for x1,x2 in insertions:
  ax.plot([x1,x2],[0.5,0.5],lw=1,color='orange')

ax.plot(dsrm1,[0,0],lw=5,color='lightblue',alpha=0.6)
ax.plot(dsrm2,[0,0],lw=5,color='lightblue',alpha=0.6)

matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()
