#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:36:19 2017

@author: selina
"""
adict={}
def appearence(s,low,high):
    if low==high:
        if s[low] not in adict:
            adict[s[low]]=0 
        else:
            adict[s[low]]+=1
        return adict
    else:
        
        if s[low] not in adict:
           adict[s[low]]=1
        adict[s[low]]+=1

        return appearence(s,low+1,high)
    
    
s= "hello world"
print(appearence(s,0,len(s)-1))