#!/usr/bin/python

import sys

total_count = 0
target_word = "fantastic"

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) == 2:
        word, count = data_mapped
        if word == target_word:
           total_count += int(count)

print("{0}\t{1}".format(target_word,total_count))

