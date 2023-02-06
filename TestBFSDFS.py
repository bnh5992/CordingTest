
from collections import deque

def bfs (graph, node, visited):
    queue = deque([node])
    visited[node] = True
    
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not (visited[i]):
                queue.append(i)
                visited[i] = True
                
def dfs(graph, start_node):
    visited = []
    need_visited = deque()
    need_visited.append(start_node)
    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
                
    return visited
graph = [
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
print()
print(dfs(graph, 1))