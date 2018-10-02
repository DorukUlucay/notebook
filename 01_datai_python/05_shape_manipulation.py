#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 20:07:42 2018

@author: dorukpc
"""

import numpy as n
# shape manipulation


# flatten
a = n.array([[1,2,3],[4,5,6],[7,8,9]])
a1 = a.ravel()
print(a1)

#reshape
a2 = a1.reshape(3,3)
print(a2)

#transpose
a2.T

# get shape
a2.shape



# stacking
c = n.array([[1,2],[3,4]])
d = n.array([[-1,-2],[-3,-4]])

stackv = n.vstack((c,d))
stackh = n.hstack((c,d))

print(stackv)
print(stackh)



# array conversion
list1 = [1,2,3,4]
arr1 = n.array(list1)
list2 = list(arr1)

# matrix kopyalama
a_copy = a.copy()
