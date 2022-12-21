#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 10:13:50 2017

@author: jsterling
"""

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

def tree_sum(root):
    if root is None: 
        return 0
    return root.data + tree_sum(root.left) + tree_sum(root.right)

def tree_max(root):
    max_val = root.data
    if root.left is not None:
        max_val = max(max_val, tree_max(root.left))
    if root.right is not None:
        max_val = max(max_val, tree_max(root.right))
    return max_val

def tree_height(root):
    if root is None: return -1
    if root.left is None and root.right is None: return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))

def print_in_order(root): # in-order traversal
    if root is None: return
    # print the left most node
    print_in_order(root.left)
    print(root.data, end=' ')
    print_in_order(root.right)
    
def in_order(root, fun): # in-order traversal
    if root is None: return
    # print the left most node
    print_in_order(root.left)
    fun(root.data, end=' ')
    print_in_order(root.right)
    
def print_bfs(root):
    todo = [root]
    while len(todo) != 0:
        next_item = todo.pop(0)
        print(next_item.data, end=' ')
        if next_item.left is not None: 
            todo.append(next_item.left)
        if next_item.right is not None: 
            todo.append(next_item.right)
    
def in_order_traverse(root): # in-order traversal
    if root is None: return
    # print the left most node
    for item in in_order_traverse(root.left):
        yield item
    yield root.data
    for item in in_order_traverse(root.right):
        yield item
    
for item in in_order_traverse(root):
    do_something(item)
    
    
  
    
    
    