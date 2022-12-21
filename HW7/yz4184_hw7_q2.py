#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 23:13:03 2017

@author: selina
"""
    

class EmptyCollection(Exception):
    pass


class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self
            self.parent = None

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)
        
    def leaves_list(self):
        if(self.root is None):
            raise Empty("Too cold the tree died. Wait for the spring comes")
        return self.subtree_leaf(self.root)
    def subtree_leaf(self,subtree_root):
        if(subtree_root.left is None and subtree_root.right is None):
            return [subtree_root.data]
        elif (subtree_root.left is not None and subtree_root.right is None):
            left= self.subtree_leaf(subtree_root.left)
            return left
        elif (subtree_root.left is None and subtree_root.right is not None):
            right=self.subtree_leaf(subtree_root.right)
            return right
        else:
            left= self.subtree_leaf(subtree_root.left)
            right=self.subtree_leaf(subtree_root.right)
            return left+right
        
    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def subtree_count(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return left_count + right_count + 1


    def sum_tree(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return left_sum + right_sum + subtree_root.data

    def height(self):
        if (self.is_empty()):
            raise EmptyCollection("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    #assuming subtree_root is not empty
    def subtree_height(self, subtree_root):
        if((subtree_root.left is None) and (subtree_root.right is None)):
            return 0
        elif(subtree_root.left is None):
            return 1 + self.subtree_height(subtree_root.right)
        elif(subtree_root.right is None):
            return 1 + self.subtree_height(subtree_root.left)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)

    def preorder(self):
        yield from self.subtree_preorder(self.root)
    
    def postorder(self):
        yield from self.subtree_postorder(self.root)
    
    def inorder(self):
        yield from self.subtree_inorder(self.root)
    
    def subtree_preorder(self,subtree_root):
        if(subtree_root is None):
            return  #or pass is okay
        else:
            yield subtree_root.data
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)
            
            
    def subtree_postorder(self,subtree_root):
        if(subtree_root is None):
            return  #or pass is okay
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postorder(subtree_root.right)
            yield subtree_root.data
    
    def subtree_inorder(self,subtree_root):
        if(subtree_root is None):
            return  #or pass is okay
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root.data
            yield from self.subtree_inorder(subtree_root.right)
           
            
    def __iter__(self):
        for node in self.inorder():
            yield node.data
        
    def breadth_first(self): #queue
        nodes_q=ArrayQueue() # add reference of node into the queue
        nodes_q.enqueue(self.root)
        while(nodes_q.is_empty()==False):
            curr_node=nodes_q.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                nodes_q.enqueue(curr_node.left)
            if curr_node.right is not None:
                nodes_q.enqueue(curr_node.right)
        
class Empty(Exception):
    pass


class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if(self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0
        
l_ch1 = LinkedBinaryTree.Node(1)
r_ch1 = LinkedBinaryTree.Node(3)
l_ch2 = LinkedBinaryTree.Node(2, l_ch1, r_ch1)
l_ch3 = LinkedBinaryTree.Node(5)
r_ch2 = LinkedBinaryTree.Node(6, l_ch3)
root = LinkedBinaryTree.Node(4, l_ch2, r_ch2)

tree = LinkedBinaryTree(root)
print(tree.leaves_list())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    