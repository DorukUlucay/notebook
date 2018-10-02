# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print.__doc__

type.__doc__

import math

# default function
def stuff(p1, p2=2):
    return p1 * p2

print(stuff(3))
print(stuff(3,2))
print(stuff(3,3))

# flexible args
def calc_stuff(p1, p2, *args):
    if(len(args))==0:
        return p1*p2
    else:
        tot=1
        for i in args:
            tot = tot * i
        tot = tot * p1 * p2
        return tot

print(calc_stuff(1,2))
print(calc_stuff(1,2,3,4))

# lambda func
sq = lambda x: x * x
sq(3)


# List
liste = [1,2,3,4,5,6,7,8]
liste[3:-1] # 4,5,6,7
liste.append(9)
liste.remove(6)
liste.reverse()


# tuple
t = (1,2,3,4,5,6,3,4,5,3)
c = t.count(3) #3


# dictionary
people = {"doruk":1, "gülten":2}
people.keys()


if "doruk" in people:
    print("doruk is here")



def getCentury(year):
    l = len(str(year))
    if l < 3:
        return 1
    elif l == 3:
        return int(str(year)[0])+1
    else:
        return int(str(year)[0:2])+1
    
print(getCentury(53))
print(getCentury(853))
print(getCentury(1443))


import math
def getCentury2(year):
    return math.floor( year / 100) + 1

    
print(getCentury2(53))
print(getCentury2(853))
print(getCentury2(1443))
print(getCentury2(14443))
