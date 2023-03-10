#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:53:31 2017

@author: selina
"""
def copy_linked_list(lnk_lst):
    new_lst=lnk_lst
    return new_lst

def deep_copy_linked_list(lnk_lst):
    new_lst=DoublyLinkedList()
    curr=lnk_lst.first_node()
    while curr!=lnk_lst.trailer:
        if type(curr.data) is not int:
            new_lst.add_last(deep_copy_linked_list(curr.data))
        
        if type(curr.data) is int:
            new_lst.add_last(curr.data)
            if curr.next!= None:
                curr=curr.next
            else:
                return new_lst
        return new_lst
    

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
    
a=DoublyLinkedList()
b=DoublyLinkedList()
b.add_last(1)
b.add_last(2)
a.add_last(b)
a.add_last(3)
print(a)
c=deep_copy_linked_list(a)
a.first_node().data.first_node().data=10
e2 = c.first_node()
e2_1 = e2.data.first_node()
print(e2_1.data)
