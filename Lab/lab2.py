#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:20:31 2017

@author: selina
"""
def powers_of_two(n):
    for i in range(1,n+1):
        yield 2**i
    
for curr_value in powers_of_two(6):
    print(curr_value)
    
