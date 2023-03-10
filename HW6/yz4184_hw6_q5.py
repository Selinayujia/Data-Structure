#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:09:25 2017

@author: selina
"""

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    new_lst=DoublyLinkedList()
    curr1=srt_lnk_lst1.first_node()
    curr2=srt_lnk_lst2.first_node()
    return merge_sublists(new_lst,srt_lnk_lst1, srt_lnk_lst2,curr1,curr2)

def merge_sublists(new_lst,srt_lnk_lst1, srt_lnk_lst2,curr1,curr2):
    if curr1==srt_lnk_lst1.trailer:
        while curr2!=srt_lnk_lst2.trailer:
            new_lst.add_last(curr2.data)
            curr2=curr2.next
        return new_lst
    elif curr2==srt_lnk_lst2.trailer:
        while curr1!=srt_lnk_lst1.trailer:
            new_lst.add_last(curr1.data)
            curr1=curr1.next
        return new_lst
    else:
        if curr1.data>curr2.data:
            new_lst.add_last(curr2.data)
            return merge_sublists(new_lst,srt_lnk_lst1, srt_lnk_lst2,curr1,curr2.next)
        elif curr1.data==curr2.data:
            new_lst.add_last(curr1.data)
            new_lst.add_last(curr2.data)
            return merge_sublists(new_lst,srt_lnk_lst1, srt_lnk_lst2,curr1.next,curr2.next)
        else:
            new_lst.add_last(curr1.data)
            return merge_sublists(new_lst,srt_lnk_lst1, srt_lnk_lst2,curr1.next,curr2)
            
    
    
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
a.add_last(2)
a.add_last(4)
a.add_last(6)

b.add_last(1)
b.add_last(1)
b.add_last(5)

print(merge_linked_lists(a,b))
