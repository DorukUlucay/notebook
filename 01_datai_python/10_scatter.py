#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 14:33:48 2018

@author: dorukpc
"""

import matplotlib.pyplot as plt
import pandas as p
iris = p.read_csv("asset01.csv")


setosa = iris[iris.Species == "Iris-setosa"]
versic = iris[iris.Species == "Iris-versicolor"]
virgin = iris[iris.Species == "Iris-virginica"]

plt.scatter(setosa.SepalLengthCm, setosa.SepalWidthCm, color="red", label="Setosa")
plt.scatter(versic.SepalLengthCm, versic.SepalWidthCm, color="green", label="Versicolor")
plt.scatter(vergin.SepalLengthCm, virgin.SepalWidthCm, color="blue", label="Virginica")

plt.legend()
plt.xlabel("Length")
plt.ylabel("Width")
plt.title("Scatter Plot")
plt.show()