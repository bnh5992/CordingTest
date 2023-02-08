
from collections import deque
def bfs(graph, start):
    dx = [-1,1,2]
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        for i in range(len(dx)):
            if i == 2:
                nx = x*dx[i]
            else:
                nx = x + dx[i]
            if nx<0 or nx>500000:
                continue
            
            if(graph[nx] == 0):
                queue.append((nx))
                graph[nx] = graph[x] + 1
            if(nx == target):
                return
graph = [0]*1000000
start,target = map(int,input().split(' '))
if(start == target):
    print(0)
elif(start > target):
    print(start-target)
else:
    bfs(graph,start)
    print(graph[target])
