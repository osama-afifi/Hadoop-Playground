#!/usr/bin/python

import sys

old_key = None
post_users = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
       continue;
    cur_key , poster = data_mapped
    if old_key and cur_key != old_key:
        print("{0}\t{1}".format(old_key, post_users))
        post_users = []
    post_users.append(poster)
    old_key = cur_key
if old_key!=None:
   for user in post_users:
       print("{0}\t{1}".format(old_key, post_users))
