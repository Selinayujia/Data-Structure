#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 12:50:36 2017

@author: selina
"""
import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size


    def extend(self, other):
        for elem in other:
            self.append(elem)


    def __getitem__(self, ind):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')

        return self.data[ind]


    def __setitem__(self, ind, val):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')

        self.data[ind] = val
        
    def insert(self,ind,val):
        if (not (0<=ind<=self.n)):
            raise IndexError('invalid index')
        else:
            if (self.n >= self.capacity):
                self.resize(2 * self.capacity)
            else:
                self.n+=1
                for i in range(self.n-1,ind,-1):
                    self.data[i]=self.data[i-1]
                self.data[ind]=val
                
    def pop1(self):
        if self.n==0:
            raise ValueError('Empty list')
        else:
            self.data[self.n-1]==None
            self.n-=1
            if self.capacity>=4*self.n:
                 self.resize(1/2 * self.capacity)
                 
    def pop2(self,ind):
        if ind>self.n:
            raise IndexError('Index out of bound')
        else:
            for i in range(ind,self.n-1):
                self.data[i]=self.data[i+1]
            self.data[self.n-1]=None
            self.n-=1
            if self.capacity>=4*self.n:
                 self.resize(1/2 * self.capacity)
                 
    def __str__(self):
        str1="["
        for i in range(self.n):
            if i is not self.n-1:
                str1+=str(self.data[i])
                str1+=","
            else:
                str1+=str(self.data[i])
        str1+="]"
        return str1
                
            
mlst = MyList()
for i in range(1, 6+1): 
    mlst.append(i)
print(mlst)
mlst.insert(3, 30)
print(mlst)
mlst.pop1()

print(mlst)
mlst.pop2(1)
print(mlst)

    
