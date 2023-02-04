num = int(input())
array = [[0]*100 for i in range(100)]
for i in range(num):
    width, hight = map(int, input().split())
    for i in range(width, width+10):
        for j in range(hight, hight+10):
            array[i][j] = 1

count = 0
for i in array:
    for j in i:
        if j == 1:
            count = count+1
        else:
            continue
print(count)

