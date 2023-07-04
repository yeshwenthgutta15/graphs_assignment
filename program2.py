#   Depth First Traversal for a Graph

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]
    
    def add_edgeing(self, source, destination):
        self.adjacency_list[source].append(destination)
    
    def depth_first_traversal(self, start_vertex):
        visited = [False] * self.vertices
        self._depth_first_traversal_recursive(start_vertex, visited)

    def _depth_first_traversal_recursive(self, current_vertex, visited):
        visited[current_vertex] = True
        print(current_vertex, end=" ")

        for adjacent_vertex in self.adjacency_list[current_vertex]:
            if not visited[adjacent_vertex]:
                self._depth_first_traversal_recursive(adjacent_vertex, visited)

# Testing the depth first traversal for a graph
graph = Graph(6)
graph.add_edgeing(0, 1)
graph.add_edgeing(0, 2)
graph.add_edgeing(1, 3)
graph.add_edgeing(2, 4)
graph.add_edgeing(2, 5)

print("Depth First Traversal:")
graph.depth_first_traversal(0)

