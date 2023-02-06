from collections import deque
qu = deque()
num = int(input())
result = []
for i in range(num):
    setting = 0
    check = 0
    count, find = map(int, input().split())
    doc = list(map(int, input().split()))
    ischeck = [False]*count
    for j in doc:
        qu.append(j)
    findnum = qu[find]
    while(True):
        if(len(qu) == 1):
            setting = setting + 1
            break
        a = qu.popleft()
        if(a < max(qu)):
            qu.append(a)
            if(find == 0):
                find = len(qu)-1
            else:
                find = find - 1
        else:
            if(a == findnum and find == 0):
                setting = setting + 1
                break
            else:
                find = find - 1
                setting = setting + 1
        

    qu.clear()
    result.append(setting)
for i in result:
    print(i)
