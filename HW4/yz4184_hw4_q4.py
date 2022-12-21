#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:04:40 2017

@author: selina
"""
def find_duplicates(lst):
    
    for i in range(0,len(lst)-1):
        if lst[i]>lst[i+1]:
            temp=lst[i]
            lst[i]=lst[i+1]
            lst[i+1]=temp
    a=lst.pop()
    countlst=[0]*a+[1]
    for i in range(len(lst)):
        b=lst[i]
        countlst[b]+=1
 
    resultlst=[]
    for j in range(1,len(countlst)):
        if countlst[j]>1:
            resultlst.append(j)
    return resultlst

a=[2,4,4,5,5,6]
print (find_duplicates(a))