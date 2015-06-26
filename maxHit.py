#!/usr/bin/python

import sys
maxi = 0
for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped)!=2:
		continue
	if(int(data_mapped[1])>maxi):
		maxi = int(data_mapped[1])
		bestHit = data_mapped[0]

print "{0}\t{1}".format(bestHit,maxi)
