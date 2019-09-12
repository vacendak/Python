# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:24:39 2019

@author: sergio sanz
"""

from turtle import *

speed(0)

r, g, b = 255, 0, 0

bgcolor("black")

for i in range(255*2):
    colormode(255)
    
    if i < 255//3:
        g += 3
        
    elif i < 255*2//3:
        r -= 3
        
    elif i < 255:
        b += 3
        
    elif i < 255*4//3:
        g -= 3
        
    elif i < 255*5//3:
        r += 3
        
    else:
        b -= 3
        
    fd(50 + i/2)
    rt(91.3)
    pencolor(r, g, b)
    