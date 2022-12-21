#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 20:39:48 2017

@author: selina
"""
def factors(num):
    lst=[i for i in range(1,int((num**1/2))+1) if num%i==0]
    lst.append(num)
    return lst

