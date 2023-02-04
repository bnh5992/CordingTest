num = int(input())
maaax = 0
result = []
answer = []
length = [0,0,0,0,0]
count = 0
winner = 0
for i in range(num):
    length[0],length[1],length[2],length[3],length[4] = map(int, input().split())
    for j in range(3):
        for k in range(j+1,5):
            for l in range(k+1,5):
                result.append((length[j]+length[k]+length[l])%10)
    if(maaax<max(result)):
        winner = i
        maaax = max(result)
    result.clear()
print(winner+1)
