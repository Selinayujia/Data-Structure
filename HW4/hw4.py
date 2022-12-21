#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 16:17:31 2017

@author: selina
"""
def e_approx(n):
    result=1.0
    current=1
    for i in range(1,n+1):
        current=current/i
        result+=current
    return result

