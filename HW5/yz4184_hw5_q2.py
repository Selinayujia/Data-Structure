#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 01:12:17 2017

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
    
class Deque:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.data = [None] * Deque.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (self.size == 0)

    def first(self):
        if self.is_empty():
            raise ('Queue is empty')
        return self.data[self.front]

    def last(self):
        back = (self.front + self.size - 1) % len(self.data)
        return self.data[back]

    def add_first(self, item):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        avail = (self.front - 1) % len(self.data)
        self.data[avail] = item
        self.front = (self.front - 1) % len(self.data)
        self.size += 1

    def add_last(self, item):
        if self.size == len(self.data):
            self.resize(2*len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data [avail] = item
        self.size += 1
        
    def pop_left(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value= self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front+ 1) % len(self.data)
        self.size -= 1
        if(self.size < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def pop_right(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        avail = (self.front + self.size-1) % len(self.data)
        value=self.data[avail]
        self.data[avail] = None
        self.size -= 1
        if(self.size < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front
        for new_ind in range(self.size):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front = 0


class midS_Stack:
    def __init__(self):
        self.stack=ArrayStack()
        self.deque=Deque()
    
    def __len__(self):
        return len(self.deque)+len(self.stack)
    
    def is_empty(self):
        return len(self.deque)+len(self.stack)==0
    
    def push(self,elem):
        self.deque.add_last(elem)
        if len(self.stack)<len(self.deque):
            self.stack.push(self.deque.pop_left())
            
    def mid_push(self,elem):
        self.deque.add_first(elem)
        if len(self.stack)<len(self.deque):
            self.stack.push(self.deque.pop_left())
    def pop(self):
        if self.deque.is_empty() and self.stack.is_empty():
            raise Empty("midS_Stack is empty")
        if self.deque.is_empty() :
            return self.stack.pop()
        return self.deque.pop_right()
        
    def top(self):
        if self.deque.is_empty() and self.stack.is_empty():
            raise Empty("midS_Stack is empty")
        if self.deque.is_empty() :
            return self.stack.data[-1]
        return self.deque.right[-1]

        
    
