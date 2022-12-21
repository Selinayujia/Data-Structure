#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 23:37:24 2017

@author: selina
"""
class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()
    
class Queue:
    def __init__(self):
        self.store=ArrayStack()
        self.data=ArrayStack()
        
    def __len__(self):
        return len(self.store)
    
    def empty(self):
        return (self.store.is_empty()) and (self.data.is_empty())

    def enqueue(self, elem):
        if (self.empty()): 
            self.store.push(elem)
        elif self.store.is_empty():
            while self.data.is_empty() is False:
                self.store.push(self.data.pop())
        else:
            self.store.push(elem)
        if len(self.store)==1:
            self.back_of_store=elem    

    def dequeue(self):
        if (self.empty()):
            raise Empty("Queue is empty")
        if self.store.is_empty():
            return self.data.pop()
        else:
            while self.store.is_empty()is False:
                self.data.push(self.store.pop())
            return self.data.pop()
        
        
   
    

Q=Queue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)


print(Q.dequeue())
print(Q.dequeue())

