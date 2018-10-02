#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:08:02 2018

@author: dorukpc
"""

# pandas bir dataframe framework'üdür.
# csv ve txt dosyaları kaynak ve hedef olarak rahatlıkla kullanılabilir
# kayıp datalar konusunda işlerimizi kolaylaştırıyormuş
# (extrapolate missing data from data-we-have durumu sanırım)
# data tranformasyonunda daha iyi bir framework
# slicing-indexing'de çok iyi
# time series'de çok iyi
# hızlı çalışmak üzere optimize edilmiş bir kütüphane


import pandas as p

dicti = {"NAME": ["Doruk", "Gülten", "Turta", "Ragnar"], 
         "AGE": [29,28,1,2],
         "MAAS": [1000,1200,100,90]}

df1 = p.DataFrame(dicti)

# header ve ilk beş satırı döndürür
df1_head = df1.head()

# .tail() da son beş satırı döndürür
# bu metotlar değer de alıp ona göre satır döndürebilirler.
df1_head3 = df1.head(3)
df1_tail3 = df1.tail(3)

#header
print(df1.columns)

print(df1.info())

print(df1.describe())

print(df1["NAME"])
#veya
print(df1.NAME)

df1["Sex"] = ["M","F","F","M"]

print(df1)

# loc konusu geniş. daha da incelenmeli.
print(df1.loc[:, "NAME":"AGE" ])