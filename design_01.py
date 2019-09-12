# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:24:39 2019

@author: sergio sanz
"""

from turtle import *

speed(0)
r, g, b = 255, 0, 0
bgcolor("black")
hideturtle()
n = int(input('Input number of sides of polygon: '))
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
    fd(15 + 0.6*i)
    rt(360/n + 1)
    pencolor(r, g, b)
done()
