#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:38:31 2017

@author: selina
"""
def permutation1(lst,low,high,empty=True):
    if empty:
        lst[low:high]
        empty=False
    if len(lst)==0:
        return[]
    elif len(lst)==1:
        return [lst]
    else:
        l=[]
        for i in range(len(lst)):
            x=lst[i]
            xs=lst[:i]+lst[i+1:]
            for j in permutation1(xs,low,high,empty):
                l.append([x]+j)
        return l
    
a=[1,2,3,4,5]
print(permutation1(a,0,4))