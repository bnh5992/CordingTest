#미완성

first = input()
second = input()
result = ''
result = result + first

for i in range(len(second)-len(first)):
    if second.count('A') < first.count('A'):
        result = result + 'A'
    else:
        result = list(result)
        result = reversed(result)
        result = ''.join(result)
        result = result + 'B'
if(result == second):
    print(1)
else:
    print(0)
print(result)
print(first.count('A'))