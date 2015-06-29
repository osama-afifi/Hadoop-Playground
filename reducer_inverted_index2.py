#!/usr/bin/python

import sys

target_word = "fantastically"

inverted_index = []
for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) == 2:
        word, index = data_mapped
        if word == target_word:
           inverted_index.append(int(index))
inverted_index.sort()    
print("{0}\t{1}".format(target_word,inverted_index))

