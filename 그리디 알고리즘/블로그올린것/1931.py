num = int(input())
playtime = []
count = 0
first = 0
for i in range(num):
    start, end = map(int, input().split())
    playtime.append([end,start])

playtimes = sorted(playtime)
for i in playtimes:
    if(i[1]>=first):
        first = i[0]
        count = count + 1
print(count)