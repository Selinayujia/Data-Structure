#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 17:49:14 2017

@author: selina
"""
def count_lowercase(s, low, high):
    if low==high:
        if ord(s[low])>96 and ord(s[low])<122:
            return 1
        else:
            return 0
    else:
        if ord(s[low])>90 and ord(s[low])<122:
            return 1+ count_lowercase(s, low+1, high)
        else:
            return 0+ count_lowercase(s, low+1, high)
def is_number_of_lowercase_even(s, low, high):
    if low==high:
        if ord(s[low])>96 and ord(s[low])<122:
            return False
        else:
            return True
    else:
        if ord(s[low])>90 and ord(s[low])<122:
            return is_number_of_lowercase_even(s, low+1, high) is False
        else:
            return is_number_of_lowercase_even(s, low+1, high) is True
            
