import sys
sys.setrecursionlimit(100000000)
n,m = map(int,input().split())
cats = list(map(int,input().split()))
lis = [ [] for _ in range(n) ]
for k in range(1,n):
    a, i = map(int,input().split())
    lis[a-1].append(i-1)
    lis[i-1].append(a-1)

def cnt(root, temp, mx, zero):
    stack = [(root, temp, mx, zero)]
    while(stack):
        spot, tmp, mxa,origin = stack.pop()
        if(visited[spot]): continue
        visited[spot] = True
        for k in lis[spot]:
            if(k != origin):
                mxy[k] = max(cats[k]*(tmp+cats[k]), mxy[spot])
                stack.append((k, cats[k]*(tmp+cats[k]), mxy[k], spot))
mxy = [0]*n
visited = [False]*n
mxy[0] = cats[0]
count = 0
cnt(0, cats[0],cats[0],0)
for k in range(n-1,0, -1):
    if(len(lis[k])==1 and mxy[k] <= m):
        count+=1
print(count)
