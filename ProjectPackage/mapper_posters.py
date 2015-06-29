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
       poster = line[3]
       print "{0}\t{1}".format(key, poster)

    else:
       key = int(line[6])
       poster = line[3]
       print "{0}\t{1}".format(key, poster)
