#       Detect Cycle in a Directed Graph

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]
    
    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)
    
    def is_cyclic(self):
        visited = [False] * self.vertices
        recursion_stack = [False] * self.vertices

        for vertex in range(self.vertices):
            if self._is_cyclic_util(vertex, visited, recursion_stack):
                return True
        
        return False
    
    def _is_cyclic_util(self, current_vertex, visited, recursion_stack):
        visited[current_vertex] = True
        recursion_stack[current_vertex] = True

        for adjacent_vertex in self.adjacency_list[current_vertex]:
            if not visited[adjacent_vertex]:
                if self._is_cyclic_util(adjacent_vertex, visited, recursion_stack):
                    return True
            elif recursion_stack[adjacent_vertex]:
                return True
        
        recursion_stack[current_vertex] = False
        return False

# Testing detect cycle in a directed graph
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 1)

has_cycle = graph.is_cyclic()
if has_cycle:
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")