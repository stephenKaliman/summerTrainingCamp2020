import sys
sys.setrecursionlimit(1000000)
n = int(input())
lis = [ [] for _ in range(n) ]
lis[0].append(0)
for k in range(1,n):
    a, i = map(int,input().split())
    lis[a-1].append(i-1)
    lis[i-1].append(a-1)

def cnt(root, count, div, zero):
    stack = [(root, count, div, zero)]
    while(stack):
        spot, depth, prb,origin = stack.pop()
        if(visited[spot]): continue
        visited[spot] = True
        for k in lis[spot]:
            if(k != origin):
                prby[k] = (depth+1)/(prb*(len(lis[spot])-1))
                stack.append((k, depth+1, prb*(len(lis[spot])-1), spot))
prby = [0]*n
visited = [False]*n
esp = 0
cnt(0, 0, 1, 0)
for k in range(n-1,0, -1):
    if(len(lis[k])==1):
        esp+=prby[k]
print(esp)
