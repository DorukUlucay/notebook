#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 21:17:25 2018

@author: dorukpc
"""

import numpy

# dizi oluştur
myArray = numpy.array([1,2,3,4,5,6,7,8])
print(myArray)

# diziyi matrise dönüştür
myMatrix = myArray.reshape(2,4)
print(myMatrix)

print(myMatrix.shape)
print(myMatrix.ndim)

# doğrudan matris tanımlama
myMatrix2 = numpy.array([[1,2,3],[3,4,5],[5,6,7]])

# matrix allocation
m3 = numpy.zeros((5,5))

m3[2,2] = 5
print(m3)



# 5 - 10 - 15 - 20 - 25 - 35 - 40 - 45
numpy.arange(10,50,5)

numpy.linspace(1, 10, 20)