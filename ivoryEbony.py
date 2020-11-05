def main():
    a, b, c = map(int,input().split())
    M = max(a,b)
    m = min(a,b)
    for i in range(0,c//M+1):
        if((c-M*i)%m==0):
            print("Yes")
            return
    print("No")

main()
