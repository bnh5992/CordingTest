from collections import deque

def bfs(graph,start):
    queue = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in start:
        queue.append(i)
    
    while queue:
        x,y = queue.popleft()

        for i in range(len(dx)):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>high-1 or ny >width-1 or nx<0 or ny<0:
                continue

            if(graph[nx][ny] == 0):
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1


width, high = map(int,input().split(' '))
tomato = []
find = []
isblank = False
for i in range(high):
    tomato.append(list(map(int,input().split(' '))))
for i in range(high):
    for j in range(width):
        if tomato[i][j] == 1:
            find.append([i,j])
bfs(tomato,find)
for i in range(high):
    for j in range(width):
        if(tomato[i][j] == 0):
            isblank = True
maximum = []
if isblank:
    print(-1)
else:
    for i in range(high):
        maximum.append(max(tomato[i]))
    print(max(maximum)-1)

