#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:15:14 2022

@author: e102136
"""

import numpy as np

graph = {}

with open('dijkstraData.txt') as f:
    data = f.readlines()
    for line in data:
        elements = list(map(str,line.split('\t')[:-1]))
        graph[str(elements[0])] = elements[1:]
f.close()



def dijkstra(graph, start, explored):
    explored[start] = 0
    frontier = {}
    while set(explored.keys()) != set(graph.keys()):
        res = dict((k, graph[k]) for k in explored.keys() if k in graph)
        flat_list = [item for sublist in list(res.values()) for item in sublist]
        flat_list = list(filter(lambda x: x.split(',')[0] not in explored.keys(), flat_list))
        nodes_on_frontier = list(map(lambda x: x.split(',')[0], flat_list))
        for node in res.keys():
            l = list(filter(lambda x: x.split(',')[0] in nodes_on_frontier, res[node]))
            for thing in l:
               if thing.split(',')[0] in frontier:
                   frontier[thing.split(',')[0]] = min(frontier[thing.split(',')[0]], explored[node] + int(thing.split(',')[1]))
               else:
                   frontier[thing.split(',')[0]] = explored[node] + int(thing.split(',')[1])
        suck_node = min(frontier, key=frontier.get)
        explored[suck_node] = frontier[suck_node]
        del frontier[suck_node]
    return explored
    
    
distances = dijkstra(graph, '1', {})

array = ['7','37','59','82','99','115','133','165','188','197']

for a in array:
    print(str(distances[a])+',')