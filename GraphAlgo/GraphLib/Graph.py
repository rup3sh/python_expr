#https://github.com/joeyajames/Python/blob/master/bfs.py
class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		
		self.distance = 9999
		self.color = 'black'
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()
	
	def get_neighbors(self):		

		return self.neighbors

class DirectedGraph:
	vertices = {}

	def get_vertex(self, vname):
		return self.vertices[vname]
			
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
			return True
		else:
			return False
			
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance))
	
	def __contains__(self, n):
		return n in self.vertices
			
	def __iter__(self):
		return iter(list(self.vertices.keys()))
		
class Graph:
	vertices = {}

	def get_vertex(self, vname):
		return self.vertices[vname]
			
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
			print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance))
	
	def __contains__(self, n):
		return n in self.vertices
			
	def __iter__(self):
		return iter(list(self.vertices.keys()))
			
	def bfs(self, vert):
		q = list()
		vert.distance = 0
		vert.color = 'red'
		for v in vert.neighbors:
			self.vertices[v].distance = vert.distance + 1
			q.append(v)
		
		while len(q) > 0:
			u = q.pop(0)
			node_u = self.vertices[u]
			node_u.color = 'red'
			
			for v in node_u.neighbors:
				node_v = self.vertices[v]
				if node_v.color == 'black':
					q.append(v)
					if node_v.distance > node_u.distance + 1:
						node_v.distance = node_u.distance + 1
						
	
	def bfsMod(self, vert, lookup):
		
		queue = collections.deque()
		queue.append(vert.name)
		vert.distance = 0
		
		while queue:
			u = queue.popleft()
			node_u = self.vertices[u]
			node_u.color = 'red'
			
			#if node_u.name == lookup:
			#	return True
				
			for v in node_u.neighbors:
				node_v = self.vertices[v]
				if node_v.color == 'black':
					queue.append(v)
					if node_v.distance > node_u.distance + 1:
						node_v.distance = node_u.distance + 1
					
					
		return False
