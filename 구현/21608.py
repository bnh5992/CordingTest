#미완성

num = int(input())
likepeople = []
All = []
peoplenum = [i+1 for i in range(num*num)]
for i in range(num*num):
    likepeople = list(map(int, input().split()))
    for n,j in enumerate(peoplenum):
        if(j == likepeople[0]):
            peoplenum[i],peoplenum[j] = peoplenum[j],peoplenum[i]
            likepeople.pop()
            All.append(likepeople)
    print(likepeople)
    print(peoplenum)