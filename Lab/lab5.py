#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 23:54:00 2017

@author: selina
"""
import ctypes
capacity=10
class Mylist:
    def __init__(self,capacity=10):
        self.data=(capacity * ctypes.py_object)()
        self.size=0
    def __len__(self):
        return self.size

    def append(self, val):
        self.data[self.size] = val
        self.size += 1
        
    
    def __setitem__(self, index, value):
        if abs(index) >= self.size:
            raise IndexError('invalid index')
        if index<0:
            self.data[self.size+index] = value
        else:
            self.data[index] = value

    def __getitem__(self, index):
        if abs(index) >= self.size:
            raise IndexError('invalid index')
        if index<0:
            return self.data[self.size+index]
        else:
            return self.data[index]

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def extend(self, other):
        for val in other.data:
            self.append(val)
    def __mul__(lst,n):
        new_lst=Mylist(n*len(lst))
        for i in range(len(new_lst)):
            new_lst[i]=lst[i%(len(lst)-1)]
    def __rmul__(n,lst):
        new_lst=Mylist(n*len(lst))
        for i in range(len(new_lst)):
            new_lst[i]=lst[i%(len(lst)-1)]
        
    def __str__(self):
        if self.size==0:
            return "[]"
        elif self.size==1:
            string="["
            string+=str(self.data[0])
            string+="]"
            return string
        else:
            string="["
            string+=str(self.data[0])
            for i in range(1,self.size):
                string+=','
                string+=str(self.data[i])
            string+="]"
            return string
    def __repr__(self):
       ", ".join(self.data) 
       
    def __add__(lst1,lst2):
        capacity=len(lst1)+len(lst2)
        new_lst=Mylist(capacity)
        for i in range(len(lst1)):
            new_lst[i]=lst1[i]
        for j in range(0,len(lst2)):
            new_lst[len(lst1)+j]=lst2[j]
        return new_lst
    def __iadd__(lst1,lst2):
        for i in range(len(lst2)):
            lst1.append(i)
        return lst1
    
    
def reverse_string(input_str,low,high):
    if low==high:
        result=input_str[high]
        return result
    else:
        out_put=reverse_string(input_str,low+1,high)
        out_put+=input_str[low]
        return out_put
    
a=reverse_string("string",0,5)
print(a)
b=Mylist()
b.append(3)
b.append(4)
b.append(5)
b[-1]=8
a=Mylist()
a.append(6)
a.append(9)
print(a)
print(b)