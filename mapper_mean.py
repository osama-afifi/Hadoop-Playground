#!/usr/bin/python

import sys
from datetime import datetime

#target_day = 6 #Sunday

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
	continue
    date, time, store, item, cost, payment = data
    weekday = datetime.strptime(date, '%Y-%m-%d').weekday()
    #if weekday == target_day:
    print "{0}\t{1}".format(weekday, cost)

