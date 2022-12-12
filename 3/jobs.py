#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 14:48:15 2022

@author: e102136
"""

with open('jobs.txt') as f:
    data = f.readlines()
    
jobs=[]
for line in data[1:]:
    weight = int(line.split()[0])
    length = int(line.split()[1])
    jobs.append([weight,length,weight - length, weight/length])
    
jobs1 = sorted(jobs, key= lambda x:(x[2], x[0]), reverse = True)
jobs2 = sorted(jobs, key= lambda x:(x[3], x[0]), reverse = True)

completion_time = 0
score = 0
for job in jobs1:
    completion_time += job[1]
    score += job[0]*completion_time
 
    
completion_time = 0
score = 0
 
for job in jobs2:
    completion_time += job[1]
    score += job[0]*completion_time