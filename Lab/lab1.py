#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:24:43 2017

@author: selina
"""
import random
def add_binary(num1_str,num2_str):
    counta=len(num1_str)
    countb=len(num2_str)
    a=int(num1_str)
    b=int(num2_str)
    decimala=0
    decimalb=0
    for i in range(counta):
        decimala+=a%10*2**i
        a=a//10
        
        
    for j in range(countb):
        decimalb+=b%10*2**j
        b=b//10
    
    resultint=decimala+decimalb
    return (str(bin(resultint))[2:])

print(add_binary("1","11"))


def can_construct(ransom_note,magazine):
    lst1=[]
    j=0
    for i in range(len(ransom_note)):
        while j< (len(magazine)):
            if ransom_note[i]==magazine[j]:
                if j not in lst1:
                    lst1.append(j)
                    break
            if j==len(magazine)-1:
                return False
            j+=1
    return True
            
print(can_construct("bb","aba"))

def create_permutation(n):
    lst=[]
    i=0
    while i<n:
        a=random.randint(0,n-1)
        if a not in lst:
            lst.append(a)
            i+=1
    return lst
print(create_permutation(6))
            
    
def scramble_word(word):
    a=len(word)
    lst=create_permutation(a)
    result=""
    for i in range(len(lst)):
        result+=word[lst[i]]
    return result
    
print(scramble_word("love"))

def fibnacci(n):
    result=[]
    b=1
    c=1
    for i in range(0,n):
        result.append(b)
        (b,c)=(c,b+c)
    return result
     

print(fibnacci(8))
        
