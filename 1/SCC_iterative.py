#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:11:00 2022

@author: e102136
"""

import collections
import sys
import random
 
def return_emptylist():
  return []
 
def return_false():
  return False
 
def ParseGraph(filename):
    #algo4SCC.txt
  """Parse a graph into a list of edges for programming Q.4
 
Args:
- filename: the on-disk graph representation
Returns:
- edges = [(vertex_1, vertex_2), ...]
"""
  edges = []
  for l in open(filename):
    fields = [int(f) for f in l.split()]
    edges.append(tuple(fields))
 
  adjacency = collections.defaultdict(return_emptylist)
  reverse_adjacency = collections.defaultdict(return_emptylist)
  for e in edges:
    adjacency[e[0]] = adjacency[e[0]] + [e]
    reverse_adjacency[e[1]] = reverse_adjacency[e[1]] + [(e[1], e[0])]
 
  return adjacency, reverse_adjacency, edges
 
t = 0
s = 0
finishing = {}
leader = {}
explored = collections.defaultdict(return_false)
def ResetState():
  global t, s, finishing, leader, explored
  t = 0
  s = 0
  finishing = {}
  leader = {}
  explored = collections.defaultdict(return_false)
 
def DFSLoop(edges, labeling, reversed = False):
  global s
  for i in labeling:
    if not explored[i]:
      s = i
      DFS(edges, i, reversed)
 
forward_adjacency = {}
reverse_adjacency = {}
def DFS(edges, start, reversed = False):
  global t
  if reversed:
    adjacency = reverse_adjacency
  else:
    adjacency = forward_adjacency
 
  # Iterative (i.e. manually managing a stack) solution.
  stack = []
  stack.append((start, 1))
 
  while len(stack) > 0:
    current, phase = stack.pop()
    if phase == 1:
      explored[current] = True
      leader[current] = s
      edge_found = False
      for edge in adjacency[current]:
        if not explored[edge[1]]:
          stack.append((current, 1))
          stack.append((edge[1], 1))
          edge_found = True
          break
      if not edge_found:
        stack.append((current, 2))
    if phase == 2:
      t += 1
      finishing[current] = t
      sys.stderr.write('Finished %s\n' % current)
 
forward_adjacency, reverse_adjacency, edges = ParseGraph("SCC.txt")
 
sys.stderr.write('Graph parsed\n')
 
num_nodes = max([e[0] for e in edges] + [e[1] for e in edges])
labeling = range(num_nodes, 0, -1)
DFSLoop(edges, labeling, True)
 
sys.stderr.write('Reverse DFSLoop done\n')
 
inverse_finishing = dict((v, k) for k, v in finishing.items())
finish_labeling = [inverse_finishing[i] for i in range(num_nodes, 0, -1)]
 
ResetState()
DFSLoop(edges, finish_labeling)
 
sys.stderr.write('Forward DFSLoop done\n')
 
sccs = {}
for i in leader:
  if leader[i] not in sccs:
    sccs[leader[i]] = [i]
  else:
    sccs[leader[i]].append(i)
 
scc=list()
for i in sccs:
  scc.append(len(sccs[i]))