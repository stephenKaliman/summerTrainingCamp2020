n = int(input())
for i in range(0,n):
    x, y, z = map(int,input().split())
    M = max(x,y,z)
    m = min(x,y,z)
    if(x^y^z!=m):
        print("NO")
        continue
    print("YES")
    print(str(M)+" "+str(m)+" "+str(1))
