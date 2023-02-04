stair = int(input())
dp = [0] * stair
arr = []
count = 0

for i in range(stair):
    score = int(input())
    arr.append(score)

if(len(arr)<=2):
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0]+arr[1]
    for i in range(2,stair):
        dp[i]=max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
    print(dp[-1])
