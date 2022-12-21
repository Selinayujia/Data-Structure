#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:07:14 2017

@author: selina
"""
def create_chain_bst(n):
    chain_bst=BinarySearchTreeMap()
    key=1
    while key!=n+1:
        chain_bst.subtree_insert(key,None)
        key+=1
    return chain_bst

def create_complete_bst(n):
    bst = BinarySearchTreeMap() 
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    if high==low:
        bst.subtree_insert(high,None)
        return 
    else:
        mid=low-high//2
        bst.subtree_insert(mid,None)
        add_items(bst,low,mid-1)
        add_items(bst,mid+1,high)
        return 
    
def restore_bst(prefix_lst):
    if len(prefix_lst)==0:
        raise Exception("The prefix list is empty")
    elif len(prefix_lst)==1:
        bst=BinarySearchTreeMap()
        item = BinarySearchTreeMap.Item(prefix_lst[0], None)
        new_node = BinarySearchTreeMap.Node(item)
        bst.root=new_node
        return 
    else:
        low=0
        high=len(prefix_lst)
        while low!=high:
            temp=prefix_lst[low]
            prefix_lst[low]=prefix_lst[high]
            prefix_lst[high]=temp
            low+=1
            high-=1
        bst=BinarySearchTreeMap()
        item1 = BinarySearchTreeMap.Item(prefix_lst.pop(), None)
        new_node1 = BinarySearchTreeMap.Node(item1)
        bst.root=new_node1
        bst.size = 1
        parent=bst.root
        
        item2 = BinarySearchTreeMap.Item(prefix_lst.pop(), None)
        new_node2 = BinarySearchTreeMap.Node(item2)
        if new_node2.key>parent.item.key:
            parent.right=new_node2
            child=parent.right
        else:
            parent.left=new_node2
            child=parent.left
        bst.size+= 1
        add_rest(bst,parent,child,prefix_lst)
            
        return
            
            
def add_rest(bst,parent,child,prefix_lst):
    if len(prefix_lst)==0:
        return bst
    suc=prefix_lst[-1]
    if suc<child.item.key:
        item = BinarySearchTreeMap.Item(prefix_lst.pop(), None)
        new_node = BinarySearchTreeMap.Node(item)
        child.left=new_node
        parent=child
        child=child.left
        bst.size+=1
        a=add_rest(bst,parent,child,prefix_lst)
        if a==bst:
            return bst 
        else:
            return add_rest(bst,parent,child,a)
            
        
    if suc>child.item.key:
        if suc<parent.item.key:
            item = BinarySearchTreeMap.Item(prefix_lst.pop(), None)
            new_node = BinarySearchTreeMap.Node(item)
            child.right=new_node
            child=child.right
            bst.size+=1
            return prefix_lst
        else:
            if parent.parent<parent or parent.parent==None:
                item = BinarySearchTreeMap.Item(prefix_lst.pop(), None)
                new_node = BinarySearchTreeMap.Node(item)
                parent.right=new_node
                child=parent.right
                bst.size+=1
                return prefix_lst
            else:
                return prefix_lst
            
        

    
def find_min_abs_difference(bst):
    if bst.root==None:
        raise Exception("The binary search tree is empty") 
    parent=bst.root
    result=helper(parent)
    return result[3]

def helper(parent):
      if parent.left==None and parent.right==None:
          return (parent.item.key,parent.item.key,None)
      if parent.left==None and parent.right!=None:
          result=helper(parent.right)
          rightmin=result[1]
          rightmax=result[2]
          count=result[3]
          newcount=abs(rightmin-parent.item.key)
          if count==None or newcount<count:
              return(parent.item.key,rightmax,newcount)
          return(parent.item.key,rightmax,count)
      if parent.left!=None and parent.right==None:
          result=helper(parent.left)
          leftmin=result[1]
          leftmax=result[2]
          count=result[3]
          newcount=abs(leftmax-parent.item.key)
          if count==None or newcount<count:
              return(leftmin,parent.item.key,newcount)
          return(leftmin,parent.item.key,count)
      if parent.left!=None and parent.right!=None:
          resultleft=helper(parent.left)
          resultright=helper(parent.right)
          leftmin=resultleft[1]
          leftmax=resultleft[2]
          rightmin=resultright[1]
          rightmax=resultright[2]
          if resultleft[3]>resultright[3]:
              count=resultright[3]
          else:
              count=resultleft[3]
          newcount1=abs(leftmax-parent.item.key)
          newcount2=abs(rightmin-parent.item.key)
          if newcount1<count:
              return (leftmin,rightmax,newcount1)
          elif newcount2<count:
              return (leftmin,rightmax,newcount2)
          else:
              return (leftmin,rightmax,count)
        
        
class BinarySearchTreeMap:

    class Item:
        def __init__(self, key, value=None):
            self.key = key
            self.value = value


    class Node:
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None
            self.leftsum=None

        def num_children(self):
            count = 0
            if (self.left is not None):
                count += 1
            if (self.right is not None):
                count += 1
            return count

        def disconnect(self):
            self.item = None
            self.parent = None
            self.left = None
            self.right = None


    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    # raises exception if not found
    def __getitem__(self, key):
        node = self.subtree_find(self.root, key)
        if (node is None):
            raise KeyError(str(key) + " not found")
        else:
            return node.item.value
    def get_ith_smallest(self,i):
        if i>self.size:
            raise IndexError("Index out of range")
        return self.leftsum(self.root,i)
    
    def leftsum(self,node,i):
        if node.leftsum-i==1:
            return node.item.key
        elif i-node.leftsum>1:
            return self.leftsum(node.right,i-1-node.leftsum)
        else: #i-node.leftsum<1:
            return self.leftsum(node.left,i)

    # returns None if not found
    def subtree_find(self, subtree_root, key):
        curr = subtree_root
        while (curr is not None):
            if (curr.item.key == key):
                return curr
            elif (curr.item.key > key):
                curr = curr.left
            else:  # (curr.item.key < key)
                curr = curr.right
        return None


    # updates value if key already exists
    def __setitem__(self, key, value):
        node = self.subtree_find(self.root, key)
        if (node is None):
            self.subtree_insert(key, value)
        else:
            node.item.value = value

    # assumes key not in tree
    def subtree_insert(self, key, value=None):
        item = BinarySearchTreeMap.Item(key, value)
        new_node = BinarySearchTreeMap.Node(item)
        if (self.is_empty()):
            self.root = new_node
            self.size = 1
        else:
            parent = self.root
            if(key < self.root.item.key):
                curr = self.root.left
            else:
                curr = self.root.right
            while (curr is not None):
                parent = curr
                if (key < curr.item.key):
                    curr = curr.left
                else:
                    curr = curr.right
            if (key < parent.item.key):
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self.size += 1
            cur=new_node
            while cur!=self.root:
                if cur.parent.left is cur:
                    cur.parent.leftsum+=1
                cur=cur.parent


    #raises exception if key not in tree
    def __delitem__(self, key):
        if (self.subtree_find(self.root, key) is None):
            raise KeyError(str(key) + " is not found")
        else:
            self.subtree_delete(self.root, key)

    #assumes key is in tree + returns value assosiated
    def subtree_delete(self, node, key):
        node_to_delete = self.subtree_find(node, key)
        value = node_to_delete.item.value
        num_children = node_to_delete.num_children()
        
        cur=node_to_delete
        while cur != self.root:
            if cur.parent.left==cur:
                cur.parent.leftsum-=1
            cur=cur.parent

        if (node_to_delete is self.root):
            if (num_children == 0):
                self.root = None
                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                if (self.root.left is not None):
                    self.root = self.root.left
                else:
                    self.root = self.root.right
                self.root.parent = None
                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        else:
            if (num_children == 0):
                parent = node_to_delete.parent
                if (node_to_delete is parent.left):
                    parent.left = None
                else:
                    parent.right = None

                node_to_delete.disconnect()
                self.size -= 1

            elif (num_children == 1):
                parent = node_to_delete.parent
                if(node_to_delete.left is not None):
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right

                child.parent = parent
                if (node_to_delete is parent.left):
                    parent.left = child
                else:
                    parent.right = child

                node_to_delete.disconnect()
                self.size -= 1

            else: #num_children == 2
                max_of_left = self.subtree_max(node_to_delete.left)
                node_to_delete.item = max_of_left.item
                self.subtree_delete(node_to_delete.left, max_of_left.item.key)

        return value

    # assumes non empty subtree
    def subtree_max(self, curr_root):
        node = curr_root
        while (node.right is not None):
            node = node.right
        return node


    def inorder(self):
        for node in self.subtree_inorder(self.root):
            yield node

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield (node.item.key, node.item.value)

