# -*- coding: utf-8 -*-

ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

def aVeryBigSum(ar):
    s=0
    i=0
    while i < len(ar):
        s+=ar[i]
        i+=1

    return s

print(aVeryBigSum(ar))