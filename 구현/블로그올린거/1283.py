
import re
num = int(input())
count = 0
insertAlpha = []
result = []
addstr = ""
isOk = False
nothing = True
for i in range(num):
    samples = list(map(str, input().split()))
    count = 0
    nothing = True
    for j in samples:
        if(count == len(samples)):
            for k in j:
                if(k in insertAlpha):
                    continue
                new_str = re.sub(k,"["+k+"]",j,1)
                new_str = re.sub(j,new_str," ".join(samples),1)
                result.append(new_str)
                insertAlpha.append(k.lower())
                insertAlpha.append(k.upper())
                nothing = False
                break
        if(j[0] not in insertAlpha):
            new_str = re.sub(j[0],"["+j[0]+"]",j,1)
            new_str = re.sub(j,new_str," ".join(samples),1)
            result.append(new_str)
            insertAlpha.append(j[0].lower())
            insertAlpha.append(j[0].upper())
            nothing = False
            break
        else:
            addstr = addstr + j
            count = count + 1
            continue
    addstr = ""
    isOk = False
    if(count == len(samples)):
        for num,j in enumerate(samples):
            if(isOk):
                break
            for k in j:
                if(k in insertAlpha):
                    continue
                new_str = re.sub(k,"["+k+"]",j,1)
                new_str = re.sub(j,new_str," ".join(samples),1)
                result.append(new_str)
                insertAlpha.append(k.lower())
                insertAlpha.append(k.upper())
                isOk = True
                nothing = False
                break
    if(nothing):
        result.append(" ".join(samples))

for i in result:
    print(i)

