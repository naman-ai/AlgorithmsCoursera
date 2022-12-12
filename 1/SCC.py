#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:04:02 2022

@author: e102136
"""
import sys
import resource

sys.setrecursionlimit(10 ** 9)
#resource.setrlimit(resource.RLIMIT_STACK, (2 ** 10, 2 ** 11))



graph = {}
rev_graph = {}
with open('SCC.txt') as f:
    data = f.readlines()
    for line in data:
        elements = list(map(str,line[:-1].split(" ")))
        try:
            (graph[elements[0]]).append(elements[1])
        except KeyError:
            graph[str(elements[0])] = [elements[1]]
        try:
            (rev_graph[elements[1]]).append(elements[0])
        except KeyError:
            rev_graph[str(elements[1])] = [elements[0]]
        if elements[0] not in rev_graph.keys():
            rev_graph[str(elements[0])] = []
        if elements[1] not in graph.keys():
            graph[str(elements[1])] = []
        
f.close()



explored = set()
s = None
finishing_time = {} 
t = 0
SCCs = {}

def DFS_rev_loop(graph):
    global explored
    for node in reversed(list(graph.keys())):
        if node not in explored:
            DFS_rev(graph , node)

def DFS_rev(graph, node):
    global finishing_time
    global explored
    global t   
    explored.add(node)
    for arc in graph[node]:
        if arc not in explored:
            DFS_rev(graph, arc)
            
    t += 1
    finishing_time[node] = t
    
def DFS_loop(graph):
    global finishing_time
    global s
    global SCCs
    global explored
    explored.clear()
    f_time = sorted(list(graph.keys()), key = lambda f_time : finishing_time[f_time],reverse=True)
    for node in f_time:
        if node not in explored:
            s = node
            SCCs[s] = 1
            DFS(graph, node)
            
def DFS(graph, node):
    global explored
    global s
    global SCCs
    explored.add(node)
    for edge in graph[node]:
        if edge not in explored:
            SCCs[s] += 1
            DFS(graph, edge)
            
            
DFS_rev_loop(rev_graph)
DFS_loop(graph)




ans = ""
sccs = sorted(list(SCCs.values()), reverse =True) 

for i in range(5):
    try:
        ans += str(sccs[i])
    except IndexError:
        ans+= "0"
    if i < 4:
        ans +=","
    
print(ans)