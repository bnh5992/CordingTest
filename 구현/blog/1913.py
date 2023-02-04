n = int(input())
find = int(input())
xindex, yindex = 0
setting = 0
flag, breaker = False
roll = 0
inside = 0
otherarray = []
count = 0
array = [[0]*n for i in range(n)]
while(n-setting != 0):
    for i in range(n-setting):
        otherarray.append(n*n-count)
        count = count + 1
    if(roll%4 == 0):
        for i in range(n-setting):
            array[i+inside][inside] = otherarray[i]
    elif(roll%4 == 1):
        for i in range(n-setting):
            array[n-setting+inside][i+inside+1] = otherarray[i]
    elif(roll%4 == 2):
        for i in range(n-setting):
            array[n-setting-i-1+inside][n-setting+inside] = otherarray[i]
    elif(roll%4 == 3):
        for i in range(n-setting):
            array[inside][n-setting-i+inside] = otherarray[i]
        inside = inside + 1
    roll = roll+1
    if(roll %2 != 0):
        setting = setting + 1
    otherarray.clear()
for i in array:
    yindex = 0
    for j in i:
        if(j == find):
            breaker = True
            break
        yindex = yindex + 1
    if(breaker):
        break
    xindex = xindex + 1 
for i in array:
    for j in i:
        print(j, end=' ')
    print('')

print(xindex+1,yindex+1)

