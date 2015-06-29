#!/usr/bin/python

import sys


old_user = None
max_val = 0
hours = []
hour_freq = [0]*24

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) !=2:
       continue;
    cur_user , cur_hour = data_mapped
    if old_user and cur_user != old_user:
       for hour in hours:
           print old_user , "\t", hour
       max_val = 0
       hour_freq = [0]*24
       hours = []

    hour_freq[int(cur_hour)] += 1
    cur_freq = hour_freq[int(cur_hour)]

    if cur_freq > max_val:
       max_val = cur_freq
       hours = [cur_hour]

    elif cur_freq == max_val:
       hours.append(cur_hour)

    old_user = cur_user

if old_user!=None:
   for hour in hours:
       print old_user , "\t", hour