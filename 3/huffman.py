#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 10:57:31 2022

@author: e102136
"""

import collections
import numpy as np
import heapq


FILE = "huffman.txt"
# FILE = "test2.txt"

fp = open(FILE, 'r')

data = fp.readlines()
n= int(data[0])

weights = data[1:]
vertices = [i for i in range(n)]

minheap = [(int(weights[i]), i) for i in range(len(weights))]

# Create a MinHeap
heapq.heapify(minheap)


while (len(minheap)>1):
    min1 = heapq.heappop(minheap)
    min2 = heapq.heappop(minheap)
    
    newweight = min1[0] + min2[0]
    newnode = (min1[1], min2[1])
    
    heapq.heappush(minheap, (newweight, newnode))
    
topNode = heapq.heappop(minheap)
