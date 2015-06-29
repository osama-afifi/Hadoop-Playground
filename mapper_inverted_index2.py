#!/usr/bin/python

import csv
import sys
import re
#import unidecode

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)


target_word = "fantastically"

for line in reader:
    words = re.findall(r"[\w]+", line[4])
    words = [x.lower() for x in words]
    words = [x.strip() for x in words]
    if target_word in words:
       print "{0}\t{1}".format(target_word, line[0])

