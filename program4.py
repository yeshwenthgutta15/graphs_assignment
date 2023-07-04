#   Count number of trees in a forest

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = [[] for _ in range(vertices)]
    
    def add_edge(self, source, destination):
        self.adjacency_list[source].append(destination)
    
    def count_trees_in_forest(self):
        visited = [False] * self.vertices
        count = 0

        for vertex in range(self.vertices):
            if not visited[vertex]:
                if self._is_tree(vertex, visited):
                    count += 1
        
        return count
    
    def _is_tree(self, current_vertex, visited):
        visited[current_vertex] = True

        for adjacent_vertex in self.adjacency_list[current_vertex]:
            if not visited[adjacent_vertex]:
                if self._is_tree(adjacent_vertex, visited):
                    return True
        
        return False

# Testing count number of trees in a forest
graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(3, 4)

tree_count = graph.count_trees_in_forest()
print("Number of trees in the forest:", tree_count)