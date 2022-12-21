#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:51:42 2017

@author: selina
""" 
class InvertedFile:
    
    def __init__(self, file_name):
        self.table=ChainingHashTableMap()
        counter=0
        none=0
        file = open(file_name, "r")
        for line in file:
            line=line.lower()
            part=line.split(" ")
            for i in range (0,len(part)):
                if part[i]==',' or part[i]=='\n':
                    none+=1
                part[i] = part[i].strip(',').strip('\n ')
                self.table[part[i]]=i+counter-none
            counter+=len(part)
                
        file.close()
        
   
        
    def indices(self, word):
        return self.table[word]
        
class ChainingHashTableMap:
    def __init__(self, N=1000):
        self.N = N
        self.table = [None] * self.N
        self.n = 0
        

    def hash_function(self, key):
        result=0
        for i in range(len(key)):
            result+=ord(key[i])
        return result
        
    def __len__(self):
        return self.n

    def __getitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            return []
        return curr_bucket[key]

    def __setitem__(self, key, value):
        j = self.hash_function(key)
        if self.table[j] is None:
            self.table[j] = UnsortedArrayMap()
            self.table[j][key] = [value]
        else:
            if self.table[j][key]==[]:
                self.table[j][key] = [value]
                
            else:
                self.table[j][key].append(value)
                
        self.n+=1

    def __delitem__(self, key):
        j = self.hash_function(key)
        curr_bucket = self.table[j]
        if curr_bucket is None:
            raise KeyError("Key Error: " + str(key))
        self.n-=len(curr_bucket[key])
        del curr_bucket[key]
        if (curr_bucket.is_empty()):
            self.table[j] = None
        

    def __iter__(self):
        for curr_bucket in self.table:
            if (curr_bucket is not None):
                for key in curr_bucket:
                    yield key

    def rehash(self, new_size):
        old = []
        for key in self:
            value = self[key]
            old.append((key, value))
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        for (key, value) in old:
            self[key] = value

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
        return []

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



        
