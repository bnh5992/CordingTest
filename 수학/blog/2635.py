num = int(input())
counts = [0,]
result = []
finalresult = []
if(num == 1):
    finalresult = [1,1,0,1]
    counts.append(4)
for i in range(1,num):
    result.clear()
    result.append(num)
    result.append(i)
    number = num
    count = 1
    first = 0
    second = i
    while(num>0):
        if(first<0):
            result.pop()
            break
        first = number
        first = first - second
        number = number - first
        second = first
        result.append(first)
        count = count + 1
    if(max(counts)>=count):
        pass
    else:
        finalresult.clear()
        counts.append(count)
        finalresult.extend(result)
print(max(counts))
for i in finalresult:
    print(i , end=" ")
