#!/usr/bin/python

import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)


for line in reader:
    if not line[0].isdigit():
        continue
    if line[5]!= 'question':
        continue
    tags = line[2].split(" ")
    for tag in tags:
        print "{0}\t1".format(tag)

