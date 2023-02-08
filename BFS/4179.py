#미완성

from collections import deque
import copy

def bfs(graph, start):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    queue = deque()
    for i in start:
        queue.append(i)
    while queue:
        x,y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>high-1 or ny >width-1 or nx<0 or ny<0:
                continue
            
            if(graph[nx][ny] == 0):
                queue.append((x,y))
                graph[nx][ny] = graph[x][y] + 1

high, width = map(int,input().split(' '))
mount = []
People = []
findFire = []
findPeople = []
for i in range(high):
    a = list(input())
    mount.append(a)
People = copy.deepcopy(mount)
for i in range(high):
    for j in range(width):
        if mount[i][j] == 'F':
            findFire.append([i,j])
            mount[i][j] = 0
            People[i][j] = 0
        if mount[i][j] == 'J':
            findPeople.append([i,j])
            mount[i][j] = 0
            People[i][j] = 0
        if mount[i][j] == '.':
            mount[i][j] = 0
            People[i][j] = 0
bfs(mount,findFire)
bfs(People,findPeople)
print(mount)
print(People)


