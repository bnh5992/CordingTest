#미완성

n = int(input())
day = [0]*(n+1)
money = [0]*(n+1)

for i in range(n):
    day[i],money[i] = map(int, input().split())

maxmoney = [0]*(n+2)
for i in range(n+1):
    maxmoney[i] = max(maxmoney[i],maxmoney[i-1])
    if(i+day[i] < n+1):
        maxmoney[i+day[i]] = max(money[i]+maxmoney[i],maxmoney[i+day[i]] )
print(maxmoney[n])
