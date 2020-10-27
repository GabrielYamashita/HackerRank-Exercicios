# -*- coding: utf-8 -*-

arr=[[1,2,3],
     [4,5,6],
     [9,8,9]]

def diagonalDifference(arr):
    arr_invertido=[]
    d_principal=0
    d_secundario=0
    
    i=0
    while i < len(arr):
        d_principal+=arr[i][i]
        arr_invertido.append(arr[i][::-1])
        d_secundario+=arr_invertido[i][i]
        i+=1
    return abs(d_principal-d_secundario)

print(diagonalDifference(arr))