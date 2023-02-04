n,k = map(int, input().split())
value = []
mins = 0
for i in range(n):
    value.append(int(input()))

revvalue = value[::-1]
for i in revvalue:
    if(k//i != 0):
        mins = mins + k//i
        k = k%i
    else:
        continue
print(mins)