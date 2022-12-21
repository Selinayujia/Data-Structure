#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 23:13:03 2017

@author: selina
"""
class EmptyTree(Exception):
    pass
def min_and_max(bin_tree):
    subtree_root=bin_tree.root
    if(subtree_root is None):
        raise EmptyTree("The tree is empty")
    return subtree_min_and_max(subtree_root)
    

def subtree_min_and_max(subtree_root):
    if(subtree_root.left is None and subtree_root.right is None):
        return (subtree_root.data,subtree_root.data)
    elif subtree_root.left is None and subtree_root.right is not None:
        right=subtree_min_and_max(subtree_root.right)
        if subtree_root.data<=right[0]<=right[1]:
            return (subtree_root.data,right[1])
        elif right[0]<=right[1]<=subtree_root.data:
            return (right[0],subtree_root.data)
        else:
            return right
    elif subtree_root.left is not None and subtree_root.right is None:
        left=subtree_min_and_max(subtree_root.left)
        if subtree_root.data<=left[0]<=left[1]:
            return (subtree_root.data,left[1])
        elif left[0]<=left[1]<=subtree_root.data:
            return (left[0],subtree_root.data)
        else:
            return left
    else:
        left=subtree_min_and_max(subtree_root.left)
        right=subtree_min_and_max(subtree_root.right)
        if left[0]<=right[0]<=right[1]<=left[1]:
            key=left
        elif right[0]<=left[0]<=left[1]<=right[1]:
            key= right
        elif left[0]<=right[0]<=left[1]<=right[1]:
            key= (left[0],right[1])
        elif left[0]<=left[1]<=right[0]<=right[1]:
            key=(left[0],right[1])
        else:
            key=(right[0],left[1])
        if subtree_root.data<key[0]:
            return (subtree_root.data,key[1])
        elif subtree_root.data>key[1]:
            return (key[0],subtree_root.data)
        else:
            return key

def is_height_balanced(bin_tree):
    if(bin_tree.root.data is None):
        raise EmptyTree("The tree is empty")
    height_biggestdiff=compare_height(bin_tree.root)
    if height_biggestdiff[1]>1:
        return False
    return True
        
    
    
def compare_height(subtree_root):
    if subtree_root.left is None and subtree_root.right is None:
        return (0,0)
    if subtree_root.left is None and subtree_root.right is not None:
        right=compare_height(subtree_root.right)
        right=(right[0]+1,right[1])
        return (right[0],right[0])
    if subtree_root.left is not None and subtree_root.right is None:
        left=compare_height(subtree_root.left)
        left=(left[0]+1,left[1])
        return (left[0],left[0])
    else:
        left=compare_height(subtree_root.left)
        left=(left[0]+1,left[1])
        right=compare_height(subtree_root.right)
        right=(right[0]+1,right[1])
        if left[0]>right[0]and left[1]>right[1]:
            return (left[0],left[1])
        elif left[0]<right[0] and  left[1]<right[1]:
            return (right[0],right[1])
        elif left[0]<right[0] and  left[1]>right[1]:
            return (right[0],left[1])
        else:
            return (left[0],right[1])

def create_expression_tree(prefix_exp_str):
    lst=prefix_exp_str.split()
    if len(lst)<3:
        raise Exception("Invalid expression str")
    else:
        low=0
        high=len(lst)-1
        while low!=high:
            temp=lst[low]
            lst[low]=lst[high]
            lst[high]=temp
            low+=1
            high-=1
        a=LinkedBinaryTree.Node("True")
        root=LinkedBinaryTree.Node(lst.pop(),a,a)
        tree=LinkedBinaryTree(helper(root,lst))
        return tree

def helper(root,lst):
    token="+-*/"
    a=LinkedBinaryTree.Node("True")
    if root.left.data=="True":
        if lst[-1] in token:
            left=LinkedBinaryTree.Node(lst.pop(),a,a)
            root.left=helper(left,lst)
            root.right=helper(root,lst)
            return root
        else:
            root=LinkedBinaryTree.Node(root.data,LinkedBinaryTree.Node(int(lst.pop())),root.right)
            root=LinkedBinaryTree.Node(root.data,root.left,helper(root,lst))
            return root
    elif root.right.data=="True":
        if lst[-1] in token:
            root=helper(LinkedBinaryTree.Node(lst.pop(),a,a),lst)
            return root
        else:
            final=LinkedBinaryTree.Node(int(lst.pop()))
            return final
    else:
        return root
    
def prefix_to_postfix(prefix_exp_str):
    tree=create_expression_tree(prefix_exp_str)
    lst=tree_postorder(tree.root)
    s=""+str(lst[0])
    for i in range(1,len(lst)):
        s+=" "+str(lst[i])
    return s
def tree_postorder(subtree_root):
    if(subtree_root is None):
        return []
    else:
        left=tree_postorder(subtree_root.left)
        right=tree_postorder(subtree_root.right)
        return left+right+[subtree_root.data]
        
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
            return []
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
    def iterative_inorder(self):
        curr=self.root
        while curr!=None:
            if curr.left ==None:
                yield curr.data
                curr=curr.right
            else:
                pre=curr.left
                while pre.right!=None and pre.right!=curr: 
                    pre=pre.right             
                if pre.right!=None: #already sorted
                    pre.right=None #break the link
                    yield curr.data
                    curr=curr.right
                else:    
                    pre.right=curr
                    curr=curr.left
        
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
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
