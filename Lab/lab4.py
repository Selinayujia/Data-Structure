#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:26:31 2017

@author: selina
"""

def is_palindrome(input_str,low,high):
    if low==high:
        return True
    else:
        if input_str[low]==input_str[high]:
            return is_palindrome(input_str,low+1,high-1)
            
        else:
            return False
        
a="kayak"
print(is_palindrome(a,0,4))

def decimal_to_binary(input_int):
    if input_int//2==0:
        return 1
    else:
        if input_int%2==1:
            return 10* decimal_to_binary(input_int//2)+1*decimal_to_binary(input_int//4)
        if input_int%2==0:
            return 10* decimal_to_binary(input_int//2)
        
print(decimal_to_binary(32))
    

def decimal_to_binary(input_int):
    if input_int//2==0 and input_int%2==1:
        return "1"
    elif input_int//2==0 and input_int%2==0:
        return "0"
    
    else:
        if input_int%2!=0:
            return  decimal_to_binary(input_int//2)+"1"
        if input_int%2==0:
            return  decimal_to_binary(input_int//2)+"0"
        
print(decimal_to_binary(32))

def solve_hanoi(n,from,to,extra):
    if n==0:
    print("move)





