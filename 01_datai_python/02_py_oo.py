#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 19:42:38 2018

@author: dorukpc
"""

class Personel:
    
    def __init__(self, name):
        self.Name = name # property'i tanımlamamış olsan da hata vermez. yaratır.
        
c = Personel("Doruk")
c.Name # çalışır. hata vermez.

# not: self'i biraz daha iyi anlamak lazım


class Character:
    
    #class variable
    Count = 0
    
    def __init__(self, name):
        self.Name = name
        self.Id = Character.Count + 1
        Character.Count = Character.Count + 1
        
c1 = Character("Ismail Vilehand")
c2 = Character("Doruk The Demon Beater")