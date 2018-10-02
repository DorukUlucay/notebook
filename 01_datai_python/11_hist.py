#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:42:19 2018

@author: dorukpc
"""

import matplotlib.pyplot as plt
import pandas as p
iris = p.read_csv("asset01.csv")


setosa = iris[iris.Species == "Iris-setosa"]
versic = iris[iris.Species == "Iris-versicolor"]
virgin = iris[iris.Species == "Iris-virginica"]

plt.hist(setosa.PetalLengthCm, bins=20)
plt.hist(versic.PetalLengthCm, bins=20)
plt.hist(virgin.PetalLengthCm, bins=20)
plt.ylabel("frekans")
plt.xlabel("değer(cm)")
plt.show()
