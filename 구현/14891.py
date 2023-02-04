#미완성

import copy
score = 0
count = 0
wheel = [[]]
b = []
state = [False,False,False,False]
for i in range(4):
    a = list(str(input()))
    for j in a:
        b.append(j)
        a = copy.deepcopy(b)
    wheel.append(a)
    b.clear()
wheel.pop(0)

def checkState(wheelnum):
    for i in range(wheelnum-1, 0, -1):
        if(wheel[i-1][2] == wheel[i][6]):
            state[i-1] = False
    for i in range(wheelnum-1,3):
        if(wheel[i][2] == wheel[i+1][6]):
            state[i+1] = False
    state[wheelnum-1] = True

num = int(input())

def roll(dir,j):
    global count
    if(dir == 1):
        wheel[j].insert(0,wheel[j][len(wheel[j])-1])
        wheel[j].pop()
        count = count + 1
    if(dir == -1):
        wheel[j].append(wheel[j][0])
        wheel[j].pop(0)
        count = count + 1

for i in range(num):
    count = 0
    state = [True,True,True,True]
    wheelnum, dir = map(int, input().split())
    checkState(wheelnum)
    for j in range(wheelnum-1, -1, -1):
        if(state[j]):
            roll(dir, j)
            dir = -dir
        else:
            break
    if(count%2 == 0):
        dir = -dir
    
    for j in range(wheelnum, 4):
        if(state[j]):
            roll(dir, j)
            dir = -dir
        else:
            break

for i in range(4):
    if(i == 0 and wheel[i][0] == '1'):
        score = score + 1
    if(i == 1 and wheel[i][0] == '1'):
        score = score + 2
    if(i == 2 and wheel[i][0] == '1'):
        score = score + 4
    if(i == 3 and wheel[i][0] == '1'):
        score = score + 8
print(score)

'''
for i in range(num):
    wheelnum, dir = map(int, input().split())
    wheelnum = wheelnum - 1
    dir = -dir
    for j in range(wheelnum-1, -1, -1):
        if(j == 0):
            if(dir == 1):
                wheel[j].insert(0,wheel[j][len(wheel[j])-1])
                wheel[j].pop()
                dir = -dir
                count = count + 1
                break
            if(dir == -1):
                wheel[j].append(wheel[j][0])
                wheel[j].pop(0)
                count = count + 1
                dir = -dir
                break
        if(wheel[j][2] == wheel[j+1][6]):
            break
        elif(dir == 1):
            wheel[j].insert(0,wheel[j][len(wheel[j])-1])
            wheel[j].pop()
            count = count + 1
            dir = -dir
        elif(dir == -1):
            wheel[j].append(wheel[j][0])
            wheel[j].pop(0)
            count = count + 1
            dir = -dir
    if(count%2 == 0):
        dir = -dir
    for j in range(wheelnum, 4):
        if(j == 3):
            if(dir == 1):
                wheel[j].insert(0,wheel[j][len(wheel[j])-1])
                wheel[j].pop()
                dir = -dir
                break
            if(dir == -1):
                wheel[j].append(wheel[j][0])
                wheel[j].pop(0)
                dir = -dir
                break
        if(wheel[j][2] == wheel[j+1][6]):
            if(dir == 1):
                wheel[j].insert(0,wheel[j][len(wheel[j])-1])
                wheel[j].pop()
                dir = -dir
            if(dir == -1):
                wheel[j].append(wheel[j][0])
                wheel[j].pop(0)
                dir = -dir
            break
        elif(dir == 1):
            wheel[j].insert(0,wheel[j][len(wheel[j])-1])
            wheel[j].pop()
            dir = -dir
        elif(dir == -1):
            wheel[j].append(wheel[j][0])
            wheel[j].pop(0)
            dir = -dir
    count = 0
'''
