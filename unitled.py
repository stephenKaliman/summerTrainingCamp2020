while(True):
    n  = input()
    if(n==''): break
    num = int(n)
    test = 1
    count = 1
    while(test%num!=0):
        test = 10*test+1
        count +=1
    print(str(count))
