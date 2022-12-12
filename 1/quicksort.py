#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 21:58:43 2022

@author: e102136
"""

import numpy as np
import math

array = open('QuickSort.txt').read().splitlines()
array = list(map(int, array))
results=np.array(array)

comparisons = 0

def quixa(array, left, right):
    length = right-left+1
    if length <= 1:
        return array[left:right+1]
    
    global comparisons
    comparisons = comparisons + length - 1
    
    #partition now#
    p = array[left]
    i = left+1
    for j in range(left+1, right+1):
        if array[j]<p:
            #swap Aj and a i
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i = i+1
    #swap a left and a i-1
    temp = array[left]
    array[left] = array[i-1]
    array[i-1] = temp
    
    array[left:i-1]=quixa(array, left, i-2)
    array[i:right+1]=quixa(array, i, right)
    
    return array[left:right+1]

quixa(results, 0, 9999)

def quixb(array, left, right):
    
    
    
    length = right-left+1
    
    if length <= 1:
        return array[left:right+1]
    
    temp = array[left]
    array[left] = array[right]
    array[right] = temp
    
    global comparisons
    comparisons = comparisons + length - 1
    
    #partition now#
    p = array[left]
    i = left+1
    for j in range(left+1, right+1):
        if array[j]<p:
            #swap Aj and a i
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i = i+1
    #swap a left and a i-1
    temp = array[left]
    array[left] = array[i-1]
    array[i-1] = temp
    
    array[left:i-1]=quixb(array, left, i-2)
    array[i:right+1]=quixb(array, i, right)
    
    return array[left:right+1]

comparisons = 0

#quixb([3,2,4,5,1], 0, 4)
quixb(results, 0, 9999)

def quixc(array, left, right):
    
    length = right-left+1
    median = math.ceil(length/2)-1
        
    
   
    if length <= 1:
        return array[left:right+1]
    
    
    
    if array[left]<array[median]<array[right] or array[left]>array[median]>array[right]:
        temp = array[left]
        array[left] = array[median]
        array[median] = temp
    elif array[left]<array[right]<array[median] or array[left]>array[right]>array[median]:
        temp = array[left]
        array[left] = array[right]
        array[right] = temp
        
    
    global comparisons
    comparisons = comparisons + length - 1
    
    #partition now#
    p = array[left]
    i = left+1
    for j in range(left+1, right+1):
        if array[j]<p:
            #swap Aj and a i
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i = i+1
    #swap a left and a i-1
    temp = array[left]
    array[left] = array[i-1]
    array[i-1] = temp
    
    array[left:i-1]=quixc(array, left, i-2)
    array[i:right+1]=quixc(array, i, right)
    
    return array[left:right+1]

comparisons = 0
#quixc([3,2,4,5,1], 0, 4)
quixc(results, 0, 9999)


