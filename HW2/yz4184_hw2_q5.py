#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:15:42 2017

@author: selina
"""
def split_parity(lst):
    count=0
    for i in range (0,len(lst)):
        if lst[i]%2!=0:
            temp=lst[count]
            lst[count]=lst[i]
            lst[i]=temp
            count+=1
    return lst
