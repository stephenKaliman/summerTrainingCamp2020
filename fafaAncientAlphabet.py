def main():
    n, m = map(int,input().split())
    S1 = list(map(int,input().split()))
    S2 = list(map(int,input().split()))
    p = 0;
    q = 1;
    mod = 1000000007
    prbq = 1;
    for i in range (0,n):
        if(S1[i]==S2[i]):
            if(S1[i]==0):
                p = (p*prbq*2*m+q*(m-1))%mod
                q = q*prbq*2*m%mod
                prbq = prbq*m%mod
            continue
        elif(S1[i]>S2[i]):
            if(S2[i]!=0):
                p = (p*prbq+q)%mod
                q = (q*prbq)%mod
                break
            p = (p*m*prbq+q*(S1[i]-1))%mod
            q = (q*prbq*m)%mod
            prbq = prbq*m%mod
        else:
            if(S1[i]!=0):
                break
            p = (p*m*prbq+q*(m-S2[i]))%mod
            q = (q*prbq*m)%mod
            prbq = prbq*m%mod
    print(p*pow(q,mod-2,mod)%mod)

main()
