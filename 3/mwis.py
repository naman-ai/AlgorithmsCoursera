#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 11:16:01 2022

@author: e102136
"""
import numpy as np

FILE = "huffman.txt"
# FILE = "test2.txt"

fp = open(FILE, 'r')

data = fp.readlines()
weights = data[1:]
weights =[int(weights[i]) for i in range(len(weights))]

a=np.array(0)
a=np.append(a,weights[0])

for i in range(2,len(weights)+1):
    candidate = max(a[i-1],a[i-2]+weights[i-1])
    a=np.append(a,candidate)
    
s={}

i=1000
while i>=1:
    if a[i-1]>=a[i-2]+weights[i-1]:
        i-=1
    else:
        s[i]=i
        i-=2