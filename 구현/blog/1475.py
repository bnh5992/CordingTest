num = str(input())
count = [0 for i in range(10)]
for i in num:
    for j in range(0,10):
        if(int(i) == j):
            count[j] = count[j] + 1
if((count[6]+count[9])%2 == 0):
    result = (count[6]+count[9])//2
else:
    result = (count[6]+count[9])//2+1
count.pop(6)
count.pop()


print(max(max(count),result))