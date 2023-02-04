
people = int(input())
laddle = int(input())
last = list(map(str, input()))
start = [chr(65+i) for i in range(people)]
sorting = []
reversing = []
result = ['?' for i in range(people-1)]
isclear = True
for i in range(laddle):
    a = list(map(str, input()))
    sorting.append(a)
reversing = sorting[::-1]
for i in sorting:
    if(i[0] == '?'):
        break
    for num,j in enumerate(i):
        if(j == '*'):
            continue
        elif(j == '-'):
            start[num], start[num+1] = start[num+1], start[num]
for i in reversing:
    if(i[0] == '?'):
        break
    for num,j in enumerate(i):
        if(j == '*'):
            continue
        elif(j == '-'):
            last[num], last[num+1] = last[num+1], last[num]

for num,i in enumerate(start):
    if(num == len(result)):
        break
    if(result[num-1] == '-'):
        result[num] = '*'
        continue
    if(i == last[num]):
        result[num] = '*'
        continue
    elif(i == last[num+1]):
        if(start[num+1]==last[num]):
            result[num] = '-'
        else:
            isclear = False
            break
    else:
        isclear = False
if(not isclear):
    result = ['x' for i in range(people-1)]

for i in result:
    print(i, end="")
