#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:55:01 2017

@author: selina
"""
def findChange(lst01):
    low=0
    high=len(lst01)-1
    mid=(low+high)//2
    if lst01[mid]==0 and lst01[mid+1]==0:
        return mid+1+findChange(lst01[mid+1:])
    elif lst01[mid]==0 and lst01[mid+1]==1:
        return mid+1
    elif lst01[mid]==1 and lst01[mid-1]==1:
        return findChange(lst01[:mid])
    elif lst01[mid]==1 and lst01[mid-1]==0:
        return mid
