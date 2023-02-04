n = int(input())
result = [0]*n
a = 0
b = 1
result[0] = a
result[1] = b
for i in range(2,n):
    result[i] = result[i-2] + result[i-1]
print(result[-1])