#!/usr/bin/python

import sys

old_user = None
cur_q_len = -1
cur_a_len = 0
a_num = 0
mean = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
       continue;

    cur_user , post_type , body_len = data_mapped
    if old_user and cur_user != old_user:
       if a_num>0:
          mean = cur_a_len/a_num
       print("{0}\t{1}\t{2}".format(old_user, cur_q_len, mean))
       cur_a_len = 0
       cur_q_len = -1
       a_num = 0
       mean = 0

    if post_type is "A":
        cur_a_len += float(body_len)
        a_num += 1
    elif post_type is "Q":
        cur_q_len = float(body_len)
    else:
        print 'WTF!'

    old_user = cur_user

if old_user!=None:
   if a_num>0:
      mean = cur_a_len/a_num
   print("{0}\t{1}\t{2}".format(old_user, cur_q_len, mean))
