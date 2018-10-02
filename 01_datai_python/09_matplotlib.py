#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 13:37:05 2018

@author: dorukpc
"""

# matplotlib: görselleştirme kütüphanesi

# csv dosyasını dataframe olarak okuyoruz
import pandas as p
iris = p.read_csv("asset01.csv")

# kolonları yazdır
print(iris.columns)

# species kolonundaki unique verileri yazdır
print(iris.Species.unique())

# sadede setosa tipindeki bitkileri alıyoruz
setosa = iris[iris.Species == "Iris-setosa"]
versico = iris[iris.Species == "Iris-versicolor"]
virginica = iris[iris.Species == "Iris-virginica"]

import matplotlib.pyplot as plt

iris_wo_index = iris.drop(["Id"], axis=1)

'''
iris_wo_index.plot()
plt.show()
'''

plt.plot(setosa.SepalLengthCm, setosa.SepalWidthCm, color="red", label="setosa")
plt.plot(versico.SepalLengthCm, versico.SepalWidthCm, color="green", label="versico")
plt.plot(virginica.SepalLengthCm, virginica.SepalWidthCm, color="blue", label="virginica")
plt.xlabel="Length"
plt.ylabel="Width"
plt.legend()
plt.show()