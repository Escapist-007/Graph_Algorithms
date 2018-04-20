"""
 Author : Md Moniruzzaman Monir

 Here, I use 'Adjacency List' approach for storing the graph. BFS is a common algorithm for searching a graph.
 In BFS, we start at the root (or another arbitrarily selected node) and explore each neighbor before going on
 to any of their children. That is, we go "WIDE" (hence breadth-first search) before we go 'DEEP'. So, we can
 think of this as searching "Level by Level" out from root.

 BFS finds the shortest path (smallest no of edges) between root and any vertex. ***

 Two class definition is used : one is 'Vertex' class and another is 'Graph' class.
 Vertex class represents the vertex objects. Every vertex stores a list of it's adjacent vertices (Neighbors).

 The "Graph" class is used because, unlike in a tree, we can't necessarily reach all nodes from a single node.
 A graph can be disconnected. In that case, we build a BFS "forest" after running BFS algo on the graph.

 Vertex color : 'white' --> Unvisited, 'grey' --> Under processing, 'black' --> Visited

"""

from collections import deque


class Vertex:
    # constructor
    def __init__(self, name):
        self.name = name
        self.color = 'white'
        self.parent_vertex_name = None
        # (smallest no of edges, or shortest path) from root to this vertex(self)
        self.distance_from_root = -1
        self.neighbors_list = []

    def add_neighbor(self, vertex_name):
        if vertex_name not in set(self.neighbors_list):
            self.neighbors_list.append(vertex_name)
            # There must be an order of the neighbors
            self.neighbors_list.sort()
            return True
        else:
            return False


class Graph:
    # constructor
    def __init__(self):
        # A dictionary (Key,Value) for storing the vertices || Key --> Vertex Name, Value --> Vertex Object
        self.vertices = {}

    def add_vertex(self, vertex_obj):
        if vertex_obj.name not in self.vertices:
            self.vertices[vertex_obj.name] = vertex_obj
            return True
        else:
            return False

    # u and v are vertex name (u -> v)
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for vertex_name in self.vertices:
                if vertex_name == u:
                    self.vertices[vertex_name].add_neighbor(v)
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
        vertex_obj.parent_vertex_name = None
        vertex_obj.distance_from_root = 0

        # Queue Data Structure (FIFO)
        queue = deque([])
        queue.append(vertex_obj)

        while True:
            if len(queue) == 0:
                break

            cur_vertex_obj = queue.popleft()

            for neighbor in cur_vertex_obj.neighbors_list:
                if self.vertices[neighbor].color == 'white':
                    self.vertices[neighbor].color = 'grey'
                    self.vertices[neighbor].parent_vertex_name = cur_vertex_obj.name
                    self.vertices[neighbor].distance_from_root = cur_vertex_obj.distance_from_root + 1
                    queue.append(self.vertices[neighbor])

            cur_vertex_obj.color = 'black'


def main():
    graph = Graph()
    root = Vertex('A')
    graph.add_vertex(root)

    # Add vertices B, C, D, E, F, G, H, I, J
    # ord('a') returns the ascii value of 'a'

    for ascii_value in range(ord('B'), ord('K')):
        graph.add_vertex(Vertex(chr(ascii_value)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

    directed_graph = False

    for edge in edges:
        if directed_graph:
            graph.add_edge(edge[:1], edge[1:])
        else:
            graph.add_edge(edge[:1], edge[1:])
            graph.add_edge(edge[1:], edge[:1])

    graph.print_graph()

    graph.breadth_first_search(root)

    print(" \n After BFS : \n ")
    print("Vertex --> Distance From Root / Parent Vertex ")
    for vertex_name in sorted(graph.vertices):
        print("  " + vertex_name + "    --> "
              + str(graph.vertices[vertex_name].distance_from_root) + " / " + str(
            graph.vertices[vertex_name].parent_vertex_name))

if __name__ == '__main__':
    main()