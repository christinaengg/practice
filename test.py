# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 22:20:19 2018

@author: tingt
"""

partners = ['a','b','c']
matrix = []
for val,partner1 in enumerate(partners):
    lst = []
    print val
    for i in range(val+1,len(partners)):
        lst.append(2)
    matrix.append(lst)
        