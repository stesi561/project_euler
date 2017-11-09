#! /usr/bin/env python3

a = 1
b = 0
x = 1
limit = 1000
while len("%d"%a) < limit:
    print("F(%d) %d: %d " % (x,len("%d"%a),a))
    c = a
    a = a+b
    b = c
    x+=1
    
