#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 10:53:36 2017

@author: selina
"""
def permutation2(lst,low,high):
    if low==high==0:
        return[[lst[low]]]
    elif len(lst)==1:
        return[lst]
    else:
        result=[]
        for i in range(high-low+1):
            e=lst[low+i]
            l=lst[:low+i]+lst[low+i+1:high+1]
            for item in permutation2(l,0,len(l)-1):
                result.append([e]+item)
        return result

a=[1,2,3]
print(permutation2(a,0,2))