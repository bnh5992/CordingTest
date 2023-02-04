#미완

num = int(input())
world = [[False]*num]*num
applenum = int(input())
snake = [[True]]
info = []
checktime= 0
tails = 1
dir = [0,0]
nowRotation = "right"
for i in range(applenum):
    x,y = map(int,input().split(" "))
    world[x][y] == True

moveCount = int(input())
for i in range(moveCount):
    time, roll = map(int, input().split(" "))
    info.append(time,roll)

def roll(rotation):
    if rotation == 'D':
        if nowRotation == "right":
            nowRotation = "down"
        elif nowRotation == "down":
            nowRotation = "left"
        elif nowRotation == "left":
            nowRotation = "up"
        elif nowRotation == "up":
            nowRotation = "right"
    elif rotation == 'L':
        if nowRotation == "right":
            nowRotation = "up"
        elif nowRotation == "up":
            nowRotation = "left"
        elif nowRotation == "left":
            nowRotation = "down"
        elif nowRotation == "down":
            nowRotation = "right"

while(True):
    for i in range(len(info)):
        if(info[i][0] == checktime):
            roll(info[i][1])
            break
    try:
        if nowRotation == "right":
            pass
        if nowRotation == "left":
            for i in range(tails+1): 
                snake[dir[0][0]][dir[0][-i]] = True
                dir[0][i] = -i
        if nowRotation == "down":
            for i in range(tails+1): 
                snake[dir[0][0]][dir[0][i]] = True
                dir[i][0] = -i
        if nowRotation == "up":
            for i in range(tails+1): 
                snake[dir[0][0]][dir[0][i]] = True
                dir[i][0] = i
            
    except:
        pass
