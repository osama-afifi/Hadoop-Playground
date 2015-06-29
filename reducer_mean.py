#!/usr/bin/python

import sys

num_count = 0
total_cost = 0
mean = 0
oldkey = None

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) == 2:
        thiskey, count = data_mapped
        if oldkey and oldkey!=thiskey:
           if num_count>0:
              mean = total_cost / num_count
           print oldkey, "\t", mean
           total_cost=0
           num_count=0
           mean=0    
        total_cost += float(count)
        num_count +=1
        oldkey = thiskey

if oldkey!=None:
   mean = total_cost / num_count
print oldkey, "\t", mean

