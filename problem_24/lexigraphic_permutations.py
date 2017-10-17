#! /usr/bin/env python3

string = '0123456789'

from itertools import permutations

x = 1
limit = 1000000
for perm in permutations(string):
    if x == limit:
        print(perm)
        break
    x+=1
    if x % 100 ==0:
        print(x)
