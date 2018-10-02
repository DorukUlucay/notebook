#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 18:15:58 2018

@author: dorukpc
"""

import numpy as n
from matplotlib import pyplot as p


x = n.array(["a","b", "c","d","e","f","g"])
y = n.array([10,20,80,85,90,150,170])

p.bar(x,y)
p.show()