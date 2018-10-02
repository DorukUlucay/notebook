#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:18:11 2018

@author: dorukpc
"""

import pandas as p


personel = {"NAME": ["Doruk", "Gülten", "Turta", "Ragnar"], 
         "AGE": [29,28,1,2],
         "MAAS": [1000,1200,100,90]}

p1 = p.DataFrame(personel)



filter_salary = p1.MAAS >= 1000
# bu işlemin çıktısı bir serie'dir.

filter_age = p1.AGE > 28

# filtreyi dataya uygulamak için
filteredData = p1[filter_salary & filter_age]

