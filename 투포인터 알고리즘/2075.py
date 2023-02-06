import heapq
n = int(input())
world = []
a = []
first = True
for i in range(n):
    world.append(list(map(int, input().split(" "))))
    if first:
        for j in world[0]:
            heapq.heappush(a,j)
        first = False
        world.pop()
        continue
    else:
        for j in world[0]:
            heapq.heappush(a,j)
            if(len(a)>n):
                heapq.heappop(a)
    world.pop()

print(heapq.heappop(a))


