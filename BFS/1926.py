from collections import deque

def bfs(graph, start):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1] 
    queue = deque()
    queue.append(start)
    area = 0
    isnothing = True
    while queue:
        x,y = queue.popleft()
        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>high-1 or ny>width-1 or nx<0 or ny<0 :
                continue

            if graph[nx][ny]==1:
                queue.append((nx,ny))
                area = area + 1 
                graph[nx][ny] = graph[x][y]+1
                isnothing = False
    if isnothing:
        return area + 1
    return area

high, width = map(int, input().split(' '))
count = 0
graph = []
for i in range(high):
    graph.append(list(map(int,input().split(' '))))
area = []
for i in range(width):
    for j in range(high):
        if(graph[j][i] == 1):
            area.append(bfs(graph,[j,i]))
            count = count + 1
print(count)
if(len(area)==0):
    print(0)
else:
    print(max(area))

