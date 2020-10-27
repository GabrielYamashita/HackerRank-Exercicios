# -*- coding: utf-8 -*-

candles=[3,2,1,3]

def birthdayCakeCandles(candles):
    a = max(candles)
    hmax_candle=0
    
    i=0
    while i < len(candles):
        if candles[i] == a:
            hmax_candle+=1
        i+=1
    return hmax_candle

print(birthdayCakeCandles(candles))