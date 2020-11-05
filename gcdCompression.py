n = int(input())
for i in range(0,n):
    m = int(input())
    array = []
    arr0 = []
    arr1 = []
    array = list(map(int,input().split()))
    for k in range(0,2*m):
        if(array[k]%2==0): arr0.append(k+1)
        else: arr1.append(k+1)
    stop = 0
    spot = 1
    if(len(arr0)==0):
        stop = 1
    while(spot<len(arr1)-stop):
        print(arr1[spot-1],arr1[spot], sep=' ')
        spot = spot+2
    spot = 1
    while(spot<len(arr0)-1+stop):
        print(arr0[spot-1],arr0[spot], sep=' ')
        spot=spot+2
            
