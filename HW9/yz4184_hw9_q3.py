#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:45:48 2017

@author: selina
"""
import random


class ChainingHashTableMap:

    def __init__(self, N=64, p=6460101079):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        self.p = p
        self.a = random.randrange(1, self.p - 1)
        self.b = random.randrange(0, self.p - 1)
        self.list=[]
        self.counter=0

    def hash_function(self, k):
        return ((self.a * hash(k) + self.b) % self.p) % self.N

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        return curr_bucket[key][0]

    def __setitem__(self, key, value):
        j = self.hash_function(key)
        if self.table[j] is None:
            self.table[j] = UnsortedArrayMap()
            self.table[j][key] = (value,self.counter)
            self.n+=1
            self.list.append(key)
        else:
            old_size = len(self.table[j])
            try:
                a=self.table[j][key]
            except KeyError:
                self.table[j][key] = (value,self.counter)
            else:
                self.table[j][key]=(value,a[1])
            new_size = len(self.table[j])
            if (new_size > old_size):
                self.n += 1
                self.list.append(key)
           
        self.counter+=1

    def __delitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        todel=self.table[j][key][1]
        del curr_bucket[key]
        self.n -= 1
        self.list[todel]=None
        if (curr_bucket.is_empty()):
            self.table[j] = None
       

    def __iter__(self):
        for i in self.list:
            if i==None:
                continue
            else:
                yield(i)
       

 


class UnsortedArrayMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    def __init__(self):
        self.table = []

    def __len__(self):
        return len(self.table)

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        for item in self.table:
            if key == item.key:
                return item.value
        raise KeyError("Key Error: " + str(key))
        

    def __setitem__(self, key, value):
        for item in self.table:
            if key == item.key:
                item.value = value
                return
        self.table.append(UnsortedArrayMap.Item(key, value))

    def __delitem__(self, key):
        for j in range(len(self.table)):
            if key == self.table[j].key:
                self.table.pop(j)
                return
        raise KeyError("Key Error: " + str(key))

    def __iter__(self):
        for item in self.table:
            yield item.key
