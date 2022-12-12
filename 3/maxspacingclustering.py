#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 13:17:49 2022

@author: e102136
"""

edges = []
with open('clustering1.txt') as f:
    vertices = int(f.readline())
    data = f.readlines()
    for line in data:
        edge = list(map(int,(line[:-1]).split()))
        edges.append(edge)
f.close()

edges.sort(key = lambda x : x[2])

clusters = 4

state = []

for i in range(1,vertices+1):
    state.append([i,[i]])

clusters_now = len(state)

def seperated(state, a, b):
    return not (b in state[a-1][1])

def merge_clusters(state, a, b):
    new_cluster = state[a-1][1] + state[b-1][1]
    for i in new_cluster:
        state[i-1][1] = new_cluster
    return state

while clusters_now!=clusters:
    edge = edges.pop(0)
    if seperated(state, edge[0], edge[1]):
        state = merge_clusters(state, edge[0], edge[1])
        clusters_now -= 1

while(True):
    edge = edges.pop(0)
    if seperated(state, edge[0], edge[1]):
        print(edge[2])
        break