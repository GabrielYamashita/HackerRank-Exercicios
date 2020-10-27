# -*- coding: utf-8 -*-

arr=[0,0,-1,1,1]

def plusMinus(arr):
    n = len(arr)
    positivo=0
    nulo=0
    negativo=0

    i=0
    while i < len(arr):
        if arr[i]<0:
            negativo+=1
        if arr[i]>0:
            positivo+=1
        if arr[i]==0:
            nulo+=1
            
        i+=1
        
    a=("{:.6f}".format(positivo/n))
    b=("{:.6f}".format(negativo/n))
    c=("{:.6f}".format(nulo/n))
        
    results=[]
    results.append(a)
    results.append(b)
    results.append(c)
        
    return results
print(plusMinus(arr))