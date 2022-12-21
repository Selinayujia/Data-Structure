#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:02:45 2017

@author: selina
"""
def split_by_sign(lst, low, high):
    if low>high:
        return lst
    else:
        if lst[low]<0:
            return split_by_sign(lst,low+1,high)
        else:
            if lst[low]>0 and lst[high]<0:
                temp=lst[low]
                lst[low]=lst[high]
                lst[high]=temp
                return split_by_sign(lst,low+1,high-1)
            else:
                return split_by_sign(lst,low,high-1)
        
a=[-1,4,2,-5,-7,8,9]
print(split_by_sign(a, 0, 6))