n = int(input())
count = 0
result = []
findmin = []
result.append(0)
result.append(1)
result.append(1)


for i in range(4,n+1):

    count = 1 + result[i-2]
    findmin.append(count)
    
    if(i%3 == 0):
        count = 1 + result[i//3-1]
        findmin.append(count)

    if(i%2 == 0):
        count = 1 + result[i//2-1]
        findmin.append(count)
    result.append(min(findmin))
    findmin.clear()

print(result[n-1])





