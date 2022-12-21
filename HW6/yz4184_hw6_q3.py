#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 23:01:58 2017

@author: selina
"""
import copy
class CompactString:
    def __init__(self, orig_str):
        self.data=DoublyLinkedList()
        temp=orig_str[0] 
        count=0
        for i in orig_str:
            if i==temp:
                count+=1
            else:
                self.data.add_last((temp,count))
                temp=i
                count=1
        self.data.add_last((orig_str[-1],count))
                
    def add(self, other):
        new_string=copy.deepcopy(self)
        if new_string.data.first_node().data[0]==other.data.last_node().data[0]:
            new_string.data.first_node().data=(new_string.data.first_node().data[0],(new_string.data.first_node().data[1]+other.data.last_node().data[1]))
            if other.data.size==1:
                return new_string
            else:
                end_of_other=other.data.trailer.prev.prev
                while end_of_other!=other.data.header:
                    new_string.data.add_first(end_of_other.data)
                    end_of_other=end_of_other.prev
        elif new_string.data.last_node().data[0]==other.data.first_node().data[0]:
             new_string.data.last_node().data=(new_string.data.last_node().data[0],(new_string.data.last_node().data[1]+other.data.first_node().data[1]))
             if other.data.size==1:
                return new_string
             else:
                 begin_of_other=other.data.header.next.next
                 while begin_of_other!=other.data.trailer:
                     new_string.data.add_last(begin_of_other.data)
                     begin_of_other=begin_of_other.next
            
        else:
            begin_of_other=other.data.header.next
            while begin_of_other!=other.data.trailer:
                new_string.data.add_last(begin_of_other.data)
                begin_of_other=begin_of_other.next
                
        return new_string

            
        

    def __lt__(self, other):
         curr1=self.data.header.next
         curr2=other.data.header.next
         if self.data.size<other.data.size: #self is smaller
             while curr1 !=self.data.trailer:  #use the shorter one as loop object
                 if curr1.data[0]==curr2.data[0]:   #if alphabet is same
                     if curr1.data[1]>curr2.data[1]: #if the number is diff, self larger amount
                         if curr2.next.data[0]>curr1.data[0]: #compare the next of other's alphabet to the current alphabet
                             return True
                         else:
                             return False
                         
                     elif curr1.data[1]<curr2.data[1]:   #if the number is diff, other larger amount
                         if curr1.next!=self.trailer:   #check if the next is going to be out of bound
                             
                             if curr1.next.data[0]>curr1.data[0]:  #if self's next alphabet larger
                                 return False
                             else:
                                 return True
                         else:
                             return True      #next is out of bound, other have more alphabet, other is larger 
                     else: 
                         pass         #same alphabet and same amount
                 else:
                     if curr1.data[0]<curr2.data[0]:   #if alphabet is diff, directly compares
                         return True  
                     else:
                         return False
                 curr1=curr1.next
                 curr2=curr2.next
             return True                #out of the loop, means the same string componet in the comparison part, because other is longer, then other is larger
         else:    #other's size is smaller or equal , use other as loop reference
             while curr2!=other.data.trailer:          
                 if curr1.data[0]==curr2.data[0]:    #alphabet is same
                     if curr1.data[1]>curr2.data[1]:  #self is larger amount
                         if curr2.next!=other.data.trailer:  #check if the next is out of bound
                             
                             if curr2.next.data[0]>curr1.data[0]:  #other's next is larger alphabet
                                 return True
                             else:
                                 return False
                         else:                #out of bound means it is last item of other, self is larger
                             return False
                         
                     elif curr1.data[1]<curr2.data[1]:       #other is in larger amount
                             
                         if curr1.next.data[0]>curr1.data[0]:    #self's next is a laregr alphabet
                             return False
                         else:
                             return True
                   
                     else:                  
                         pass          #same alphabet same amount
                 else:
                     if curr1.data[0]<curr2.data[0]:        #self's alphabet direc smaller
                         return True
                     else:                
                         return False
                 curr1=curr1.next
                 curr2=curr2.next
             return False    #out the loop means self larger or equal while self have larger size
            
    def __le__(self, other):
        curr1=self.data.header.next
        curr2=other.data.header.next
        if self.data.size<other.data.size: #self is smaller
             while curr1 !=self.data.trailer:  #use the shorter one as loop object
                 if curr1.data[0]==curr2.data[0]:   #if alphabet is same
                     if curr1.data[1]>curr2.data[1]: #if the number is diff, self larger amount
                         if curr2.next.data[0]>curr1.data[0]: #compare the next of other's alphabet to the current alphabet
                             return True
                         else:
                             return False
                         
                     elif curr1.data[1]<curr2.data[1]:   #if the number is diff, other larger amount
                         if curr1.next!=self.trailer:   #check if the next is going to be out of bound
                             
                             if curr1.next.data[0]>curr1.data[0]:  #if self's next alphabet larger
                                 return False
                             else:
                                 return True
                         else:
                             return True      #next is out of bound, other have more alphabet, other is larger 
                     else: 
                         pass                               
                 else:
                     if curr1.data[0]<curr2.data[0]:   #if alphabet is diff, directly compares
                         return True  
                     else:
                         return False
                 curr1=curr1.next
                 curr2=curr2.next
             return True                #out of the loop, means the same string componet in the comparison part, because other is longer, then other is larger
        else:    #other's size is smaller or equal , use other as loop reference
             while curr2!=other.data.trailer:          
                 if curr1.data[0]==curr2.data[0]:    #alphabet is same
                     if curr1.data[1]>curr2.data[1]:  #self is larger amount
                         if curr2.next!=other.trailer:  #check if the next is out of bound
                             
                             if curr2.next.data[0]>curr1.data[0]:  #other's next is larger alphabet
                                 return True
                             else:
                                 return False
                         else:                #out of bound means it is last item of other, self is larger
                             return False
                         
                     elif curr1.data[1]<curr2.data[1]:       #other is in larger amount
                             
                         if curr1.next.data[0]>curr1.data[0]:    #self's next is a laregr alphabet
                             return False
                         else:
                             return True
                     else: 
                        print("else")
                        if curr2.next==other.data.trailer:
                             print("if")
                             if curr1.next==self.data.trailer:
                                 return True
                             else: 
                                 return False
                        else:
                             pass
                 else:
                    if curr1.data[0]<curr2.data[0]:
                        return True
                    else:
                        return False
                 curr1=curr1.next
                 curr2=curr2.next
            

    def __gt__(self, other):
        curr1=self.data.header.next
        curr2=other.header.next
        if self.data.size<other.data.size:
            while curr1 !=self.data.trailer:
                if curr1.data[0]==curr2.data[0]:
                    if curr1.data[1]>curr2.data[1]:
                        if curr2.next.data[0]>curr1.data[0]:
                            return False
                        else:
                            return True
                         
                    elif curr1.data[1]<curr2.data[1]:
                        if curr1.next!=self.trailer:
                             
                            if curr1.next.data[0]>curr1.data[0]:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else: 
                        continue
                else:
                    if curr1.data[0]<curr2.data[0]:
                        return False
                    else:
                        return True
            return False
        else:
             while curr2 !=other.data.trailer:
                 if curr1.data[0]==curr2.data[0]:
                     if curr1.data[1]>curr2.data[1]:
                         if curr2.next!=other.trailer:
                             
                             if curr2.next.data[0]>curr1.data[0]:
                                 return True
                             else:
                                 return False
                         else:
                             return False
                         
                     elif curr1.data[1]<curr2.data[1]:
                             
                         if curr1.next.data[0]>curr1.data[0]:
                             return False
                         else:
                             return True
                   
                     else: 
                         continue
                 else:
                     if curr1.data[0]<curr2.data[0]:
                         return True
                     else:
                         return False
             return False

    def __ge__(self, other):
        curr1=self.data.header.next
        curr2=other.header.next
        if self.data.size<=other.data.size:
            while curr1 !=self.data.trailer:
                if curr1.data[0]==curr2.data[0]:
                    if curr1.data[1]>curr2.data[1]:
                        if curr2.next!=self.trailer:
                            if curr2.next.data[0]<curr1.data[0]:
                                return True
                            else:
                                return False
                        else:
                            return True
                         
                    elif curr1.data[1]<curr2.data[1]:
                         if curr1.next!=self.trailer:
                             
                             if curr1.next.data[0]>curr1.data[0]:
                                 return True
                             else:
                                 return False
                         else:
                             return False
                    else: 
                         pass
                else:
                    if curr1.data[0]<curr2.data[0]:
                        return False
                    else:
                        return True
            return False
        elif self.data.size>other.data.size:
            while curr2 !=other.data.trailer:
                if curr1.data[0]==curr2.data[0]:
                    if curr1.data[1]>curr2.data[1]:
                        if curr2.next!=other.trailer:
                             
                            if curr2.next.data[0]>curr1.data[0]:
                                return False
                            else:
                                 return True
                        else:
                            return True
                         
                    elif curr1.data[1]<curr2.data[1]:
                             
                        if curr1.next.data[0]>curr1.data[0]:
                            return True
                        else:
                            return False
                   
                    else: 
                        pass
                else:
                    if curr1.data[0]<curr2.data[0]:
                        return False
                    else:
                        return True
            return False        
    
    def __str__(self):
        curr= self.data.header.next
        s=str(curr.data)
        while curr.next!=self.data.trailer :
            s+="-->"
            curr=curr.next
            s+=str(curr.data)
        return s
    def __repr__(self): 
        return str(self)
    
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
    
    
    
s=CompactString('aaabb')
a=CompactString('aaabb')
b=s.add(a)
print(s<a)
print(s<=a)
print(b)