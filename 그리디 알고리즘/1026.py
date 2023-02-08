num = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
result = []
B.sort()
for i in range(len(A)):
    result.append(B[i]*max(A))
    A.pop(A.index(max(A)))
print(sum(result))