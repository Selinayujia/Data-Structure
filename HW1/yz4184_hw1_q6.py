#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 16:51:42 2017

@author: selina
"""
class Vector:
    def __init__(self,d):
        self.coords=[0]*d

    def __sub__(self,other):
        if (len(self)!=len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for i in range (len(self)):
            result[i]=self[i]-other[i]
        return result
    def __neg__(self):
        result = Vector(len(self))
        for i in range (len(self)):
            result[i]=-self[i]
        return result
    def __rmul__(self,num):
        result =Vector(len(self))
        for i in range (len(self)):
            result[i]=3*result[i]
        return result
    def __mul__(self,param):
        if param.type==int:
            result =Vector(len(self))
            for i in range (len(self)):
                result[i]=param*result[i]
            return result
        elif param.type==self.type:
            if (len(self)!=len(param)):
                raise ValueError("dimensions must agree")
            dotproduct=0
            for j in range(len(self)):
                dotproduct+=self[j]*param[j]
            return dotproduct
        else:
            raise TypeError("Please give an integer or Vector")
    def __repr__(self):
        return 'Vector(d=%s)' % (self.coords)
            
            
            
                    
                    
                    
                    
                
        
