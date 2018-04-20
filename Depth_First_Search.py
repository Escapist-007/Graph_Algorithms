"""
 Author : Md Moniruzzaman Monir

"""

class Vertex:

    def __init__(self, name):
        self.name = name
        self.color = 'white'            
        self.discover_time = 0
        self.finish_time = 0
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
    
    def __init__(self):
        # A dictionary (Key,Value) for storing the vertices || Key --> Vertex Name, Value --> Vertex Object
        self.vertices = {}    
        self.time = 0

    def add_vertex(self, vertex_obj):
        if vertex_obj.name not in self.vertices:
            self.vertices[vertex_obj.name] = vertex_obj
            return True
        else:
            return False

    # u and v are vertex name. (u -> v)
    def add_edge(self, u, v):  
        if u in self.vertices and v in self.vertices:
            for vertex_name in self.vertices:
                if vertex_name == u:
                    self.vertices[vertex_name].add_neighbor(v)
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

    def depth_first_Search(self, root):
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
        if directed_graph == True:
            graph.add_edge(edge[:1], edge[1:])
        else:
            graph.add_edge(edge[:1], edge[1:])
            graph.add_edge(edge[1:], edge[:1])

    graph.print_graph()

    graph.depth_first_Search(root)

    # Print timestamps of each vertex
    print(" \n After DFS : \n ")
    print("Vertex --> Discover Time / Finish Time")
    for vertex_name in sorted(graph.vertices):
        print("  " + vertex_name + "    --> " +
              str(graph.vertices[vertex_name].discover_time) + " / " + str(graph.vertices[vertex_name].finish_time))

if __name__ == '__main__':
    main()