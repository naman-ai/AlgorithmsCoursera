#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 20:22:09 2022

@author: e102136
"""

with open('edges.txt') as f:
    data = f.readlines()

nNodes = data[0].split()[0]
nEdges = data[0].split()[1]


graph = []
for line in data[1:]:
    graph.append(line.split())

X = ['1']
T = []

V = list(map(str, range(1, 501)))

while set(X)!=set(V):
    #frontier = graph[graph[0] is in X and graph[1]is not in X]
    frontier = list(filter(lambda x: (((x[0] in X) and (not(x[1] in X))) or ((x[1] in X) and (not(x[0] in X)))), graph))
    edge = min(frontier, key = lambda t: int(t[2]))
    T.append(edge)
    if edge[0] in X:
        X.append(edge[1])
    else:
        X.append(edge[0])
    
sum(int(n) for _,_,n in T)
