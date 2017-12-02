#!/bin/python3

#https://github.com/joeyajames/Python/blob/master/

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		
		self.discovery = 0
		self.finish = 0
		self.color = 'black'
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	vertices = {}
	time = 0
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
			return True
		else:
			return False
			
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].discovery) + "/" + str(self.vertices[key].finish))

	'''def _dfs(self, vertex):
		global time
		vertex.color = 'red'
		vertex.discovery = time
		time += 1
		for v in vertex.neighbors:
			if self.vertices[v].color == 'black':
				self._dfs(self.vertices[v])
		vertex.color = 'blue'
		vertex.finish = time
		time += 1
		
	def dfs(self, vertex):
		global time
		time = 1
		self._dfs(vertex)
	'''
		
	def dfsMod(self, vertex):
		
		time = 1
		print("Running dfs modified..")
		
		def _dfsInternal(vertex):
			nonlocal time 
			vertex.color = 'red'
			vertex.discovery = time
			time += 1
			print ("Visited:", vertex.name)
			for v in vertex.neighbors:
				if self.vertices[v].color == 'black':
					_dfsInternal(self.vertices[v])
			vertex.color = 'blue'
			vertex.finish = time
			time += 1
		
		_dfsInternal(vertex)
		
	def dfsStack(self, vertex):
	
		time = 1
		print("DFS with Stack...")
		stack =[]
		stack.append(vertex.name)
		while stack:
			
			vname = stack.pop()
			v = self.vertices[vname]			
			v.color = 'red'
			v.discovery = time
			time+=1
			print ("Visited:", vname)
			
			for n in v.neighbors:
				if self.vertices[n].color == 'black':
					stack.append(n)

			v.color='blue'
			v.finish = time
			time+=1		
				
		
			
g = Graph()
# print(str(len(g.vertices)))
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])
	
g.dfsMod(a)
#g.dfsStack(a)
#g.print_graph()
