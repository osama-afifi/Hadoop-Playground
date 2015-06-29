#!/usr/bin/python

import csv
import sys


reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if not line[0].isdigit():
        continue

    if line[5] == 'question': # node type
       key = int(line[0])
       bod_len = len(line[4])
       print("{0}\tQ\t{1}".format(key, bod_len))

    if line[5] == 'answer': # node type
       key = int(line[6])
       bod_len = len(line[4])
       print("{0}\tA\t{1}".format(key, bod_len))
