# -*- coding: utf-8 -*-

n = 6

def staircase(n):
    i=1
    while i < n+1:
        a = n - i
        print((a)*" " + i*"#")
        i+=1
        
staircase(n)