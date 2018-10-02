#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 12:00:38 2018

@author: dorukpc
"""

import pandas as p
import numpy as n

personel = {"NAME": ["Doruk", "Gülten", "Turta", "Ragnar"], 
         "AGE": [29,28,1,2],
         "MAAS": [1000,1200,100,90]}

p1 = p.DataFrame(personel)

# pandas mean
print(p1.MAAS.mean())

# numpy mean with pandas dataframe
print(n.mean(p1.MAAS))


avg_maas = p1.MAAS.mean()

# ortalama maaştan yüksek ya da düşük olma durumuna göre yeni kolon açan kod. list comprehension.
p1["above_avg"] = ["yüksek" if each > avg_maas else "düşük" for each in p1.MAAS]

# benim alternatif çözümüm
above_avg_filter = p1.MAAS > avg_maas
p1["above_avg_doruk"] = above_avg_filter

# drop col
p1.drop(["above_avg"], axis=1, inplace=True)
p1.drop(["above_avg_doruk"], axis=1, inplace=True)

# concat vertical
p2 = p.concat([p1.tail(1), p1.head(1)], axis=0)

#concat horizontal
p3 = p.concat([p1.MAAS, p1.AGE], axis =1)


# apply ile transformation
def years_before_adult(age):
    return 18 - age

p1["is_adult"] = p1.AGE.apply(years_before_adult)    