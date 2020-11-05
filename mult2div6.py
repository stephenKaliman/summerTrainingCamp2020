import math

n = int(input())
for i in range(0,n):
    x = int(input())
    count = 0
    count2 = 0
    mod = 1
    while (x%(mod*6)==0):
        mod = mod*6
        count = count+1
    while (x%(mod*3)==0):
        mod = mod*3
        count2 = count2+1
    if(x != mod):
        print(-1)
        continue
    print(2*count2+count)
    
