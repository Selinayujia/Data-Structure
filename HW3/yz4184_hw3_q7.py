#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 19:23:08 2017

@author: selina
"""
a=[]
def flat_list1(nested_lst, low, high):
    if low>high:
        return a
    else:
        if type(nested_lst[low])==list:
            return flat_list1(nested_lst[low],0,len(nested_lst[low])-1)
        else:
            a.append(nested_lst[low])
            return flat_list1(nested_lst,low+1,high)




def flat_list(nested_lst, low, high):
    i=0
    while i in range(low,high+1): 
        if i==high:
            if type(nested_lst[low])==list:
                return flat_list(nested_lst[low],0,len(nested_lst[low])-1)
            else:
                return (nested_lst[low])
        else:
            if type(nested_lst[i])==list:
                flat_list(nested_lst[i],0,len(nested_lst[i])-1)
            else:
                a=[i]
                
                a+[flat_list(nested_lst,low+1,high)]



b=[1,2,3]
print(flat_list(b, 0, 2))