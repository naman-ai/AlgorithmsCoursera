#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:41:51 2022

@author: e102136
"""

from heapq import heapify, heappush, heappop

with open('Median.txt') as f:
    data = f.readlines()
    elements = list(map(int,data))
  
min_heap = []
max_heap = []

heapify(min_heap)
heapify(max_heap)
total = elements[0]
heappush(max_heap, 0-elements[0])

for i in range(1,len(elements)):
    new_input = elements[i]
    if len(min_heap) == len(max_heap):
        element = heappop(min_heap)
        element2 = 0-heappop(max_heap)
        a=sorted((new_input, element, element2))
        heappush(max_heap, 0-a[0])
        heappush(max_heap, 0-a[1])
        heappush(min_heap, a[2])
        total=total-max_heap[0]
    elif len(min_heap) > len(max_heap):
        element = heappop(min_heap)
        heappush(min_heap, max(new_input, element))
        heappush(max_heap, max(0-new_input, 0-element))
        total=total-max_heap[0]
    elif len(min_heap) < len(max_heap):
        element = 0-heappop(max_heap)
        heappush(min_heap, max(new_input, element))
        heappush(max_heap, max(0-new_input, 0-element))
        total=total-max_heap[0]