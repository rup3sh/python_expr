#!/bin/python3

import collections
from GraphLib import Graph

													
g = Graph.Graph()
a = Graph.Vertex('A')
g.add_vertex(a)
g.add_vertex(Graph.Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.add_vertex(Graph.Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])
	
g.bfs(a)
#isFound = g.bfsMod(a, 'I')
#isFound = g.bfsMod(a, 'X')
#print ("Node found:", isFound)

g.print_graph()
