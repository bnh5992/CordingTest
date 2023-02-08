
#서렌이요
#gg
class Fire:
    n = 0
    world = []
    def __init__(self,_r,_c,_m,_s,_d) -> None:
        self.r =_r
        self.c = _c
        self.m = _m
        self.s = _s
        self.d = _d
        
    @staticmethod
    def worldsetting():
        Fire.world = [[0 for j in range(n)] for i in range(n)]
    def setting(self):
        Fire.world[self.r][self.c] = self.m

    def move(self):
        dx = [0,1,1,1,0,-1,-1,-1]
        dy = [-1,-1,0,1,1,1,0,-1]
        nx = self.c + dx[self.d] * self.s
        ny = self.r + dy[self.d] * self.s
        nx,ny = Fire.exchange(nx,ny)
        self.c = nx
        self.r = ny
    @staticmethod
    def exchange(nx,ny):
        if nx>len(Fire.world)-1:
            nx = nx % len(Fire.world)
        if ny >len(Fire.world)-1:
            ny = ny % len(Fire.world)
        if nx < 0:
            if(abs(nx) % len(Fire.world) == 0):
                nx = 0
            else:
                nx = len(Fire.world) - abs(nx) % len(Fire.world)
        if ny < 0:
            if(abs(ny) % len(Fire.world) == 0):
                ny = 0
            else:
                ny = len(Fire.world) - abs(ny) % len(Fire.world)
        return nx, ny

    


n,m,k = map(int,input().split(" "))
Fire.n = n
info = []
Fire.worldsetting()
for i in range(m):
    a = list(map(int,input().split(' ')))
    info.append(Fire(a[0]-1,a[1]-1,a[2],a[3],a[4]))
dxa = [-1,1,1,-1]
dya = [1,1,-1,-1]
dx2 = [1,0,-1,0]
dy2 = [0,1,-0,-1]
for i in range(k):
    a = 0
    x = 0
    y = 0
    seperate = 0
    infoCount = len(info)
    for j in range(len(info)-4*seperate):
        info[j].move()
    while a != infoCount-1:
        combineweight = 0
        combineSpeed = 0
        count = 0
        oddCount = False
        evenCount = False
        isdelete = False
        for b in range(a,len(info)-1):
            for d in range(b+1,len(info)):
                if info[b].r == info[d].r and info[b].c == info[d].c:
                    combineweight = combineweight + info[a].m
                    combineSpeed = combineSpeed + info[a].s
                    count = count + 1
                    if(info[a].d %2 == 0):
                        evenCount = True
                    else:
                        oddCount = True
                    for c in range(a+1,len(info)-1):
                        if info[a].r == info[c].r and info[a].c == info[c].c:
                            isdelete = True
                            combineweight = combineweight + info[c].m
                            combineSpeed = combineSpeed + info[c].s
                            count = count + 1
                            if(info[c].d %2 == 0):
                                evenCount = True
                            else:
                                oddCount = True
                            del info[c]
                odd = 1
                for c in range(4):
                    if(count == 0):
                        break
                    if(evenCount and oddCount):
                        nx, ny = Fire.exchange(info[a].r+dxa[c],info[a].c+dya[c])
                        info.append(Fire(nx,ny,combineweight//5,combineSpeed//count,odd))
                    else:
                        nx, ny = Fire.exchange(info[a].r+dx2[c],info[a].c+dy2[c])
                        info.append(Fire(nx,ny,combineweight//5,combineSpeed//count,odd-1))
                    odd = odd + 2
                if isdelete:
                    del info[a]
                    seperate = seperate + 1
                c = 0
                while c <= len(info)-1:
                    if(info[c].m == 0):
                        del info[c]
                    c = c + 1
        a = a+1
result = 0
for i in range(len(info)):
    result = result + info[i].m
print(result)

for i in range(len(info)):
    info[i].setting()