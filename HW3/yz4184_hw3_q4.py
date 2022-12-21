#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:12:39 2017

@author: selina
"""
def list_min(lst, low, high):
    if low==high:
        return lst[low]
    else:
        if lst[low]<lst[low+1]:
            temp=lst[low+1]
            lst[low+1]=lst[low]
            lst[low]=temp
            return list_min(lst,low+1,high)
        else:
            return list_min(lst,low+1,high)
             
            
a=[2,4,5,6,2,5,3,9,1]
print(list_min(a,0,8))
