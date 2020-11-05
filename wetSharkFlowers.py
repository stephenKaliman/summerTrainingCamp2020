n, p = map(int,input().split())
count = 0
l = []
r = []
prb = []
for i in range(0,n):
    li, ri = map(int,input().split())
    l.append(li-1)
    r.append(ri)
l.append(l[0])
r.append(r[0])
for i in range(0,n+1):
    prb.append((r[i]//p-l[i]//p)/(r[i]-l[i]))
for i in range(0,n):
    count = count + 1-(1-prb[i])*(1-prb[i+1])
print(2000*(count))
