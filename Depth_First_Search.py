
    # Author : Md Moniruzzaman Monir

class Vertex:

    def __init__(self, name):
        self.name = name                 # Name of the vertex
        self.color = 'white'             # 'white' --> Unvisited, 'grey' --> Under processing, 'black' --> Visited
        self.discover_time = 0
        self.finish_time = 0
        self.neighbors_list = []         # List of adjacent vertices (neighbors)
        # print("Vertex " + str(self.name) + " created" )

    def add_neighbor(self, vertex_name):
        if vertex_name not in set(self.neighbors_list):
            self.neighbors_list.append(vertex_name)
            self.neighbors_list.sort()    # There must be an order of the neighbors
            return True
        else:
            return False


class Graph:

    def __init__(self):
        self.vertices = {}    # A dictionary (Key,Value) for storing the vertices. Here, Key --> Vertex Name and Value --> Vertex Object
        self.time = 0

    def add_vertex(self, vertex_obj):
        if vertex_obj.name not in self.vertices:
            self.vertices[vertex_obj.name] = vertex_obj
            return True
        else:
            return False

    def add_edge(self, u, v):  # u and v are vertex name. (u -> v)
        if u in self.vertices and v in self.vertices:
            for i in self.vertices:
                if i == u:
                    self.vertices[i].add_neighbor(v)
            return True
        else:
            return False

    def print_graph(self):  # 'Adjacency List' representation
        print()
        print("Vertex --> Neighbors")
        for i in sorted(list(self.vertices)):
            print("  " + i + "    --> " + str(self.vertices[i].neighbors_list))

    '''
        Depth First Search
    '''

    def dfs(self, root):
        global time
        time = 1
        self.dfs_visit(root)

    def dfs_visit(self, vertex_obj):
        global time
        vertex_obj.color = 'grey'
        vertex_obj.discover_time = time
        time = time + 1
        # Explore all of it's neighbors
        for neighbor in vertex_obj.neighbors_list:
            if self.vertices[neighbor].color == 'white':
                self.dfs_visit(self.vertices[neighbor])
        vertex_obj.color = 'black'
        vertex_obj.finish_time = time
        time = time + 1

    '''
    Driver code
    '''

# Here g is a Unweighted graph

g = Graph()
root = Vertex('A')
g.add_vertex(root)

for i in range(ord('B'), ord('E')):     # Add vertices B, C, D
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AC', 'AD', 'BD']

directed_graph = True   # Track if the graph is directed or undirected

for e in edges:

    if directed_graph == True:
        g.add_edge(e[:1], e[1:])
    else:
        g.add_edge(e[:1], e[1:])
        g.add_edge(e[1:], e[:1])

g.print_graph()

g.dfs(root)  # Depth-First Search on g

# Print timestamps of each vertex
print()
print("Vertex --> Discover Time / Finish Time")
for i in sorted(list(g.vertices)):
    print("  " + i + "    --> " + str(g.vertices[i].discover_time) + " / " + str(g.vertices[i].finish_time))

