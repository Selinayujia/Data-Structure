#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 21:14:34 2017

@author: selina
"""
import copy
class EmptyCollection(Exception):
    pass


class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def first_node(self):
        if (self.is_empty()):
            raise EmptyCollection("List is empty")
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
            raise EmptyCollection("List is empty")
        return self.trailer.prev

    def add_first(self, elem):
        return self.add_after(self.header, elem)

    def add_last(self, elem):
        return self.add_after(self.trailer.prev, elem)

    def add_after(self, node, elem):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node()
        new_node.data = elem
        new_node.prev = prev
        new_node.next = succ
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_before(self, node, elem):
        return self.add_after(node.prev, elem)

    def delete(self, node):
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def __iter__(self):
        if(self.is_empty()):
            return
        cursor = self.first_node()
        while(cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '[' + '<-->'.join([str(elem) for elem in self]) + ']'

    def __repr__(self):
        return str(self)
    
class Integer:
    def __init__(self, num_str):
        self.data=DoublyLinkedList()
        for i in num_str:
            self.data.add_last(i)
    def __add__(self, other):
        if self.data.size >= other.data.size:
            new_integer=copy.deepcopy(self)
            current1=other.data.last_node()
            current=new_integer.data.last_node()
            while current1 != other.data.header:
                a=int(current.data)
                b=int(current1.data)
                if (a+b)>9:
                    if current.prev==new_integer.data.header:
                        new_integer.data.add_first("1")
                    else:
                        current.data=str((a+b)%10)
                        current.prev.data= str(int(current.prev.data)+1)
                else:
                    current.data=str(a+b)
                current=current.prev
                current1=current1.prev
            
        else:
             new_integer=copy.deepcopy(other)
             current1=new_integer.data.last_node()
             current=self.data.last_node()
             while current!= self.data.header:
                 a=int(current1.data)
                 b=int(current.data)
                 if (a+b)>9:
                    if current.prev==new_integer.data.header:
                        new_integer.add_first("1")
                    else:
                        current1.prev.data= str(int(current1.prev.data)+1)
                        current1.data=str((a+b)%10)
                 else:
                     current1.data=str(a+b)
                 current=current.prev
                 current1=current1.prev
                 
        testbegin=new_integer.data.last_node()
        while testbegin!=new_integer.data.header:
            if testbegin.data=="10":
                    
                if testbegin.prev==new_integer.data.header:
                       
                    new_integer.data.add_first("1")
                    testbegin.data="0"
                else:
                    testbegin.data="0"
                    testbegin.prev.data= str(int(testbegin.prev.data)+1)
            testbegin=testbegin.prev
        return new_integer   
    def __str__(self):
        curr= self.data.first_node()
        s=""
        while curr!=self.data.trailer:
            s+=curr.data
            curr=curr.next
        return s
    def __repr__(self): 
        return str(self)
a=Integer("99")
b=Integer("123")
print(a)
print(b)
c=a+b
print(c)
   
