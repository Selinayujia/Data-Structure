#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 17:45:21 2017

@author: selina
"""
def __sumPow__(n):
    sum=0
    for i in range(n):
        sum+=i**2
    return sum
    
sum[i**2 for i in range(n)]

def __sumOddPow__(n):
    sum=0
    for i in range(n):
        if i%2!=0:
            sum+= i**2
    return sum

sum[i**2 for i in range(n) if i%2!=0]
