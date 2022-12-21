#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 21:34:33 2017

@author: selina
"""
def two_sum(srt_lst, target):
    low=0
    high=len(srt_lst)-1
    for i in range(len(srt_lst)):
        if srt_lst[low]+srt_lst[high]<target:
            low+=1
        elif srt_lst[low]+srt_lst[high]>target:
            high-=1
        else:
            return(low,high)
