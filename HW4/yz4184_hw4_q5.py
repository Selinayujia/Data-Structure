#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:37:52 2017

@author: selina
"""
def remove_all(lst,value): 
    low=0
    high=len(lst)-1
    count=0
    while low<high or low==high:
        if lst[low]==value and lst[high]!=value:
            temp=lst[low]
            lst[low]=lst[high]
            lst[high]=temp
            low+=1
            high-=1
            count+=1
        elif lst[low]!=value and lst[high]==value:
            low+=1
            high-=1
            count+=1
        elif lst[low]==value and lst[high]==value:
            high-=1
            count+=1
        else:
            low+=1
    if count==0:
        raise ValueError 
    else: 
        while count>0:
            lst.pop()
            count-=1
    return lst
        
a=[1,2,3,4,5]
print(remove_all(a,2))