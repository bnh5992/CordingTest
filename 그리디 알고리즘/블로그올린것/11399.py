people = int(input())

time = list(map(int, input().split()))
times = sorted(time,reverse=False)
result = 0
for i in range(people):
    result = result + sum(times)
    times.pop()

print(result)