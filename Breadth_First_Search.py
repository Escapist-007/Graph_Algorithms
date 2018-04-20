
'''
 Author : Md Moniruzzaman Monir
'''

from collections import  deque

class Vertex:

    def __init__(self, name):

        self.name = name
        self.color = 'white'

        self.parent_vertex = None
        self.distance_from_root = -1

        self.neighbors_list = []

    def add_neighbor(self, vertex_name):

        if vertex_name not in set(self.neighbors_list):
            self.neighbors_list.append(vertex_name)
            self.neighbors_list.sort()
            return True
        else:
            return False

class Graph:

    def __init__(self):
        self.vertices = {}   # A dictionary (Key,Value) for storing the vertices. Here, Key --> Vertex Name and Value --> Vertex Object

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


    def print_graph(self):
        print()
        print("Vertex --> Neighbors")
        for i in sorted(list(self.vertices)):
            print("  " + i + "    --> " + str(self.vertices[i].neighbors_list))

    '''
        Breadth First Search
    '''

    def breadth_first_search(self, vertex_obj):
        vertex_obj.color = 'grey'
        vertex_obj.parent_vertex = None
        vertex_obj.distance_from_root = 0

        queue = deque([])
        queue.append(vertex_obj)

        while True:

            if len(queue) == 0:
                break

            cur_vertex_obj = queue.popleft()

            for i in cur_vertex_obj.neighbors_list:
                if self.vertices[i].color == 'white':
                    self.vertices[i].color = 'grey'
                    self.vertices[i].parent_vertex = cur_vertex_obj
                    self.vertices[i].distance_from_root = cur_vertex_obj.distance_from_root + 1
                    queue.append(self.vertices[i])

            cur_vertex_obj.color = 'black'




'''
 Driver code
'''

graph = Graph()
root  = Vertex('A')
graph.add_vertex(root)

for i in range(ord('B'), ord('F')):     # Add vertices B, C, D, E
    graph.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AC', 'AD', 'BD', 'AE', 'CD', 'CE', 'DB', 'EB']

directed_graph = True   # Track if the graph is directed or undirected

for edge in edges:
    if directed_graph == True:
        graph.add_edge(edge[:1], edge[1:])
    else:
        graph.add_edge(edge[:1], edge[1:])
        graph.add_edge(edge[1:], edge[:1])

graph.print_graph()
graph.breadth_first_search(root)


for key in sorted(list(graph.vertices.keys())):
    print(key + str(graph.vertices[key].neighbors_list) + "  " + str(graph.vertices[key].distance_from_root))





