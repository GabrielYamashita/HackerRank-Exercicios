# -*- coding: utf-8 -*-

a=[5, 6, 7]
b=[3, 6, 10]

def compareTriplets(a,b):
    p_a=0
    p_b=0
    i=0
    while i < len(a):
        if a[i]<b[i]:
            p_b+=1

        elif a[i]>b[i]:
            p_a+=1

        else:
            pass

        i+=1
    resultados=[]
    resultados.append(p_a)
    resultados.append(p_b)
    return resultados

print(compareTriplets(a,b))