#Breadth First Traversal for a Graph:
from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]
    
    def add_edgeing(self, source, destination):
        self.adjacency_list[source].append(destination)
    
    def breadth_first_traversaling(self, vertex_starting):
        visited = [False] * self.vertices
        queue = deque()
        queue.append(vertex_starting)
        visited[vertex_starting] = True

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            for adjacent_vertex in self.adjacency_list[current_vertex]:
                if not visited[adjacent_vertex]:
                    queue.append(adjacent_vertex)
                    visited[adjacent_vertex] = True

# Testing the breadth first traversal for a graph
graph = Graph(6)
graph.add_edgeing(0, 1)
graph.add_edgeing(0, 2)
graph.add_edgeing(1, 3)
graph.add_edgeing(2, 4)
graph.add_edgeing(2, 5)

print("Breadth First Traversal:")
graph.breadth_first_traversaling(0)