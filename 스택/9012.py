num = int(input())
result = []
stack = []
Nothing = True
for i in range(num):
    bracket = input()
    for j in bracket:
        if(j == ")"):
            try:
                stack.pop()
            except:
                Nothing = False
                break
        else:
            stack.append(j)
    if(len(stack) == 0 and Nothing):
        result.append("YES")
    else:
        result.append("NO")
    stack.clear()
    Nothing = True
for i in result:
    print(i)