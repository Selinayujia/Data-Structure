#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 15:19:00 2017

@author: selina
"""        
class DoublyLinkedList:
    class Node:
        def __init__(self,data=None, next=None,prev=None):
            self.data=data
            self.next=next
            self.prev=prev
        
    def _init_(self):
        self.header=DoublyLinkedList.Node()
        self.trailer=DoublyLinkedList.Node()
        self.header.next=self.trailer
        self.trailer.prev= self.header
        self.size=0
        
dll=DoublyLinkedList.Node()

        
head=None

head= Node()


head.data=1
head.next=Node()
head.next.data=2

head.next.next=Node()
head.next.next.data=3

cursor=head
while(cursor is not None):
    print(cursor.data)
    cursor=cursor.next

new_node=None()
new_node.data=4
new_node.next=head
head=new_node

def add_first(lnk_lst,elem):
    new_node = Node()
    new_node.data=elem
    new_node.next=lnk_lst
    return new_node

    
input()