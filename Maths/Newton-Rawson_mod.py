# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:28:49 2019

@author: sergio sanz
"""
import math

def round_half_up(n, decimals = 0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier

x = float(input('Input a number: '))
eps = float(input("Input an approx.(for neg. exp. of 10 use '1e-nn'): "))
prec = int(input('Input precision decimals (must be equal to exp. of 10): '))
print()
ite = 0
low = 0.0
high = x
ans = (high + low) / 2.0

while abs(ans ** 2 - x) >= eps:
    # print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    ite += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
ans = round_half_up(ans, prec)
print('Iterations = ' + str(ite))
print(str(ans) + ' is close to square root of ' + str(x) + ' by ' + str(prec) \
      + ' decimals of precision. ')
