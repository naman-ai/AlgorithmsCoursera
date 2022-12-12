#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  6 15:40:06 2022

@author: e102136
"""
import numpy as np

array = open('_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt').read().splitlines()
results = list(map(int, array))
results=np.array(results)

def sortandcount(array, n):
    if n==1:
        return array, 0
    else:
        half = int(n/2)
        b, x = sortandcount(array[:half], half)
        c, y = sortandcount(array[half:], n-half)
        d, z = mergeandcount(b, c, n)
        return d, (x+y+z)
    
def mergeandcount(b, c, n):
    i=0
    j=0
    bsize = b.size
    csize = c.size
    invs = 0
    d=np.zeros(n)
    for k in range(n):
        if ((i<bsize) and (j<csize) and (b[i]<c[j])) :
            d[k] = b[i]
            i += 1
        elif (i<bsize) and (j<csize) and (b[i]>c[j]):
            d[k] = c[j]
            j += 1
            invs += bsize-i
        elif i==bsize:
            d[k] = c[j]
            j += 1
        elif j==csize:
            d[k] = b[i]
            i += 1
            
            
    return d, invs

