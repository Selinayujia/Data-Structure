#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 21:28:50 2017

@author: selina
"""
class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()
mydict={}   
def post_fix_calculator():
    s=input('-->')
    if s=="done()":
        return
    else:
        operators=['+','-','*','/']
        S=ArrayStack()
        lst = s.split()
        if len(lst)==1:
            if 48<ord(lst[0])<58:
                print(lst[0])
            if 96<ord(lst[0])<123:
                print(mydict[lst[0]])
                
                
                
        elif lst[1]=="=":
            for token in range(2,len(lst)):
                if(lst[token] not in operators):
                    if 48<ord(lst[token])<58:
                        S.push(int(lst[token]))
                    else:
                        S.push(mydict[lst[token]])
                           
                else:
                    arg2=S.pop()
                    arg1=S.pop()
                    if(lst[token]=='+'):
                        res =arg1+arg2
                    elif(lst[token]=='-'):
                        res=arg1-arg2
                    elif(lst[token]=='*'):
                        res=arg1*arg2
                    else:
                        res=arg1/arg2
            
                    S.push(res)
            mydict[lst[0]]=S.pop()
            print(lst[0])
            
            
            
        else:
            for token in lst:
                if(token not in operators):
                  
                    if 48<ord(token)<58:
                        S.push(int(token))
                    else:
                        S.push(mydict[token])
                else:
                    arg2=S.pop()
                    arg1=S.pop()
                    if(token=='+'):
                        res =arg1+arg2
                    elif(token=='-'):
                        res=arg1-arg2
                    elif(token=='*'):
                        res=arg1*arg2
                    else:
                        res=arg1/arg2
            
                    S.push(res)
            print(S.pop())
    return post_fix_calculator()



post_fix_calculator()
              
               
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   
           