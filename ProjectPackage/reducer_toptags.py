#!/usr/bin/python

import sys

hits_count = 0
old_key = None
top10 = [("",0)]*10

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    this_key , this_count = data_mapped

    if old_key and old_key != this_key:
       if hits_count > top10[9][1]:
          top10[9] = (old_key, hits_count)
          top10.sort(key=lambda x : x[1], reverse=True)
       hits_count = 0

    old_key = this_key
    hits_count += int(this_count)

if old_key != None:
   if hits_count > top10[9][1]:
      top10[9] = (old_key, hits_count)
      top10.sort(key=lambda x : x[1], reverse=True)

for tag,count in top10:
    print("{0}\t{1}".format(tag,count))


