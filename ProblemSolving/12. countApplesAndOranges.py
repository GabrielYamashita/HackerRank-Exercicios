# -*- coding: utf-8 -*-

s, t = 7, 11
a, b = 5, 15
# m, n = 3, 2
apples = [-2, 2, 1]
oranges = [5, -6]

def countApplesAndOranges(s, t, a, b, apples, oranges):
    home = range(s,t+1)
    maca_home=0
    laranja_home=0
    
    i=0
    while i < len(apples):
        hit = a + apples[i]
        if hit in home:
            maca_home += 1
        i+=1
    
    i=0
    while i < len(oranges):
        hit = b + oranges[i]
        if hit in home:
            laranja_home += 1
        i+=1

    print(maca_home)
    print(laranja_home)
        
countApplesAndOranges(s, t, a, b, apples, oranges) 