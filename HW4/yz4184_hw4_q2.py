#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:06:48 2017

@author: selina
"""
import copy
result=[]
def permutations(lst,low,high):
     if low>high:
         return result
     else:
         head=[]
         head.append(lst[low])
         smallst= copy.copy(lst)
         smallst.remove(lst[low])
         
         if len(smallst)>2:
             for i in permutations(smallst,0,len(smallst)-1):
                  result.append([head]+i)
             return permutations(lst,low+1,high)
             
            
         elif len(smallst)==2:
             lst1=head+smallst
             
             temp=smallst[0]
             smallst[0]=smallst[1]
             smallst[1]=temp
             
             lst2=head+smallst
             result.append(lst1)
             result.append(lst2)
             return permutations(lst,low+1,high)
         
         else:
             tail=[]
             tail.append(smallst[0])
             lst1=head+tail
             result.append(lst1)
             
             return permutations(lst,low+1,high)
         
a=[1,2,3,4]
print(permutations(a,0,3))
        
        
