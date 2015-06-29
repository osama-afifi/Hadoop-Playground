__author__ = 'Osama'

#!/usr/bin/python

import csv
import sys
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if str(line[3]).isdigit():
       date = line[8]
       date = date[:19]
       hour = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').hour
       userid = line[3]
       print "{0}\t{1}".format(userid, hour)
