a = int(input())
result = 0

while(a%5 != 0):
    if(a//3 == 0):
        if(a%3 == 0):
            result = result + 1
            break
        else:
            result = -1
            break
    result = result + 1
    a = a - 3
if(a%5 == 0):
    result = result + a//5
print(result)



