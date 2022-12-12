#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 14:04:31 2022

@author: e102136
"""

# =============================================================================
# array = open('kargermincut_data.txt').read().splitlines()
# array = list(map(int, array))
# results=np.array(array)
# 
# =============================================================================
import random

graph = {}
with open('kargermincut_data.txt') as f:
    data = f.readlines()
    for line in data:
        elements = list(map(str,line.split('\t')[:-1]))
        graph[str(elements[0])] = elements[1:]
        
f.close()
iterations = 10000



def min_cut(graph1, iterations):
    cuts=[]
    for i in range(iterations):
        graph = graph1.copy()
        while len(graph)>2:
            node_a, list_a = random.choice(list(graph.items()))
            node_b = random.choice(list_a)
            graph = merge(node_a, node_b, graph)
            
        node, list_cut = random.choice(list(graph.items()))
        cuts.append(len(list_cut))
    
    return min(cuts)

def merge(node_a, node_b, graph):
    list_a = graph[node_a]    
    list_b = graph[node_b]
    list_merged = list(list_a + list_b)
    list_merged = list(filter(lambda a: a != node_a, list_merged))
    list_merged = list(filter(lambda a: a != node_b, list_merged))
    new_node = node_a+'+'+node_b
    graph[new_node] = list_merged
    del graph[node_a], graph[node_b]
    for key in graph.keys():
        graph[key] = [new_node if (x==node_a or x==node_b) else x for x in graph[key]]
    return graph

print(min_cut(graph, iterations))