class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
        else:
            print("One or both vertices do not exist in the graph.")

    def display(self):
        for vertex in self.vertices:
            print(vertex, "-->", " ".join(map(str, self.vertices[vertex])))

class Lucas_graph:
    def __init__(self) -> None:
        self.vertices = []
        self.edges = []
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            if self.has_edge(vertex1,vertex2):
                print("The edge is already there.")
            else:
                self.edges.append([vertex1,vertex2])
        else:
            print("One or both vertices do not exist in the graph.")

    def display(self):
        for vertex in self.vertices:
            vertex_connections = []
            for edge in self.edges:
                check_edges = []
                if edge[0] != vertex:
                    check_edges.append(edge[0])
                if edge[-1] != vertex:
                    check_edges.append(edge[-1])
                if len(check_edges) == 1:
                    vertex_connections.append(check_edges[0])
            print(f"The vertex {vertex} is connected to {vertex_connections}")
    
    def has_edge(self, vertex1, vertex2):
        if len(self.edges) == 0: return False
        for edge in self.edges:
            if vertex1 in edge and vertex2 in edge:
                return True
            else:
                return False

# Example usage:
graph = Lucas_graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

print("Graph representation:")
graph.display()

def binary_search(sorted_list, target):
    """ Tree """
    min_side = 0
    max_side = len(sorted_list) - 1
    while min_side <= max_side:
        mid = (min_side + max_side) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            min_side = mid + 1
        else:
            max_side = mid -1

    return -1
