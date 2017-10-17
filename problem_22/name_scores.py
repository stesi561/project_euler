#! /usr/bin/env python3

import sys

raw_names = ""
with open(sys.argv[1], 'r') as f:
    raw_names = f.read()

names = raw_names.split('","')
names[0] = names[0].strip('"')
names[-1] = names[-1].strip('"')
names.sort()
name_scores_sum = 0
for x in range(len(names)):
    n = names[x]
    name_scores_sum+= (1+x)*sum([ord(y)-64 for y in n])

print(name_scores_sum)
