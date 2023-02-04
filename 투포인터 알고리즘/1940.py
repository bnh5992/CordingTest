
n = int(input())
find = int(input())
nums = list(map(int, input().split(" ")))
num = sorted(nums)
count = 0
point1 = 0
point2 = n-1
while(True):
    if(point2 == point1):
        break
    if(num[point1]+num[point2] == find):
        count = count + 1
        point1 = point1 + 1
        continue
    if(num[point1]+num[point2] >= find):
        point2 = point2 - 1
        continue
    elif(num[point1]+num[point2] < find):
    
        point1 = point1 + 1
print(count)

