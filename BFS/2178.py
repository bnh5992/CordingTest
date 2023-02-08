from collections import deque
def bfs(graph, start):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1] 
    queue = deque()
    queue.append(start)
    while queue:
        x,y = queue.popleft()
        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>high-1 or ny>width-1 or nx<0 or ny<0 :
                continue

            if graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1
                
    

high, width = map(int, input().split(' '))
graph = []
for i in range(high):
    graph.append(list(map(int,str(input()))))

bfs(graph,[0,0])
print(graph[high-1][width-1])
print(graph)
