
high, width = map(int, input().split(' '))
samples = list(map(int, input().split()))
count = 0
result = 0
ischeck = False
isblank = True

for i in range(high):
    count = 0
    while count != width:
        isblank = True
        if(samples[count]>=1):
            for j in range(count+1, width):
                if(samples[j] <= 0):
                    result = result + 1
                elif(samples[j]>=1):
                    isblank = False
                    count = j-1
                    break
            if(isblank):
                result = result - width + count + 1
        count = count + 1
    samples = list(map(lambda x: x-1, samples))

print(result)

