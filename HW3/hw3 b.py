#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:41:47 2017

@author: selina
"""
def print_oposite_triangles(n):
    if n==1:
       print('*')
    else:
        print('*'*n)
        print_oposite_triangles(n-1)
        print('*'*n)
print_oposite_triangles(4)