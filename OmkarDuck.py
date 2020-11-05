import sys
 
n = int(input())
row = []
for x in range(0,n):
    row.append(0)
for r in row:
    print(r, end = ' ')
print()
sys.stdout.flush()
for y in range(2,n+1):
    for x in range(0,n-1):
        row[x] = row[x+1]+pow(2,2*n-2-x-y)
        print(row[x], end=' ')
    if(y!=n): print(0)
    else: print(2**(n-1)-1)
    sys.stdout.flush()
 
q = int(input())
for t in range(0,q):
    a = int(input())
    c = [1,1]
    print(*c)
    for i in range(2*n-3,-1,-1):
        if(a&pow(2,i)): c[0]+=1
        else: c[1]+=1
        print(*c)
    



