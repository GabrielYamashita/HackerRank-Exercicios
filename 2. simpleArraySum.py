# -*- coding: utf-8 -*-

ar = [1, 2, 3, 4, 10, 11]

def simpleArraySum(ar):
    i=0
    s=0
    while i < len(ar):
        s+= ar[i]
        i+=1   
    return s

print(simpleArraySum(ar))