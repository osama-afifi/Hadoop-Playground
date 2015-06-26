#!/usr/bin/python

import sys

hitsCount = 0
oldPath = None

# Loop around the data
# It will be in the format key\val
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        continue

    thisPath = data_mapped
    if oldPath and oldPath != thisPath:
        print oldPath, "\t", hitsCount
        oldPath = thisPath;
        hitsCount = 0

    oldPath = thisPath
    hitsCount += 1

if oldPath != None:
    print oldPath, "\t", hitsCount

