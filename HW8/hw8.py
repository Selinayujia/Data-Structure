#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 16:10:27 2017

@author: selina
"""
def recreate_tree(preorder,inorder):
    pre=preorder
    ino=inorder
    i=0
    while i!=len(ino):
        if ino[i]==pre[0]:
            break
        i+=1
    left=ino[:i]
    right=ino[i+1:]
    
    
    
    
    
    
    

    
  
    
    
    
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
a=[DBACEGF]
b=[ABCDEFG]        



        
l_ch1 = LinkedBinaryTree.Node(1)
r_ch1 = LinkedBinaryTree.Node(4)
l_ch2 = LinkedBinaryTree.Node(6, l_ch1, r_ch1)
ch = LinkedBinaryTree.Node(8)
l_ch3 = LinkedBinaryTree.Node(7,None,ch)

r_ch2 = LinkedBinaryTree.Node(2, l_ch3)
root = LinkedBinaryTree.Node(5, l_ch2, r_ch2)

tree = LinkedBinaryTree(root)
  
    
for node in tree.subtree_postorder(root):
    print(node)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    