#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:00:58 2017

@author: selina
"""
def print_triangle(n):
    if n==1:
        print('*'*n)
    else:
        print_triangle(n-1)
        print('*'*n)
    
def print_oposite_triangles(start,n):
    if start==n:
        print(start*'*')
    else:
        print(start*'*') 
        print_oposite_triangles(start+1,n)
        print(start*'*') 
print_oposite_triangles(1,5)