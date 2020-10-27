# -*- coding: utf-8 -*-

s="07:05:45PM"

def timeConversion(s):
    indicador= (s[8]+s[9])
    mins_segs= (s[2]+s[3]+s[4]+s[5]+s[6]+s[7])
    
    if indicador == "AM":
        if s[0]+s[1] == "12":
            return "00"+mins_segs
        else:
            tempo= (s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6]+s[7])
            return tempo

    if indicador == "PM":
        if s[0]+s[1] == "12":
            return "12"+mins_segs
        else:
            horas=int(s[0]+s[1])
            horas+=12
            horas=str(horas)
            return horas+mins_segs

print(timeConversion(s))