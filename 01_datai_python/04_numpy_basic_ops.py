#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:42:25 2018

@author: dorukpc
"""

import numpy as n

a = n.array([1,2,3])
b = n.array([4,5,6])

print(a+b)
print(a-b)
print(b-a)
print(a**b)

print(n.sin(a))

print(a<2)


ma = n.array([[1,2,3],[4,5,6]])
mb = n.array([[1,2,3],[4,5,6]])

print(ma*mb)

n.sqrt(629)

msq = n.array([9,16,25,36,49,64])
print(n.sqrt(msq))


#indexing ve slicing
# reverse
print(msq[::-1])

# box selection
b = n.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(b[1:3,1:3])

# son satırı al
print(b[-1,:])
#indexing ve slicing-son