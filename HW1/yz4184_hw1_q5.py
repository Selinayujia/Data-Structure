#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 18:17:45 2017

@author: selina
"""
def __fibs__(n):
    a=0,b=0,c=1
    while a<n:
        yield b
        (b,c)=(c,b+c)
        a+=1