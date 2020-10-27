# -*- coding: utf-8 -*-

arr = [1,2,3,4,5]

def miniMaxSum(arr):
    somas=[]
    
    i=0
    filtro=0
    while i < len(arr):
        s=0
        j=0
        while j < len(arr):
            s += arr[j]
            j+=1
        
        s-=arr[filtro]
        somas.append(s)
        
        i+=1
        filtro+=1
        
    print(min(somas),max(somas))

miniMaxSum(arr)