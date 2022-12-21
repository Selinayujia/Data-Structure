#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:36:28 2017

@author: selina
"""
def __shift__(lst, num):
    for i in range(num):
        lst.append(lst[0])
        lst.pop(0)
    return lst
        
def TwoSideShift(lst, num, direct=None):
    if direct is  None:
        for i in range(num):
            lst.append(lst[0])
            lst.pop(0)
            
    elif direct== "right":
        for i in range(num):
            lst.insert(0,lst[-1])
            lst.pop()


    elif direct== "left":
        for i in range(num):
            lst.append(lst[0])
            lst.pop(0)
    return lst
   
        
a=[1,2,3,4,5]
print(TwoSideShift(a, 2,"right"))
            
