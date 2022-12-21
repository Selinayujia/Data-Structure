#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:19:47 2017

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

class Max_Stack:
    def __init__(self):
        self.stack=ArrayStack()
        self.max_indicator=0
    def __len__(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, val):
        if self.is_empty():
            self.max_indicator=val
            self.stack.push( (val,self.max_indicator) )
        else:
            self.stack.push((val,self.max_indicator) )
            if val>self.max_indicator:
                self.max_indicator=val

    def top(self):
        if (self.is_empty()):
            raise Empty("Max_Stack is empty")
        return self.stack.data[-1][0]
        
    
    def pop(self):
        if (self.is_empty()):
            raise Empty("Max_Stack is empty")
        else:
            self.max_indicator=self.stack.top()[1]
            return self.stack.pop()[0]
            
        
    def max(self):
        return self.max_indicator
    
    
a=Max_Stack()
a.push(8)
a.push(1)
a.push(6)
a.push(10)
print(a.max())
print(a.pop())
print(a.max())
