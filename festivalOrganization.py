import math

def choose(n,k):
    p1 = 1
    p2 = 1
    if(n<k or n<0 or k<0):
        return 0
    if(k<n//2):
        for i in range(1,k+1):
            p1 = p1*i
            p2 = p2*(n+1-i)
    else:
        for i in range(1,n-k+1):
            p1 = p1*i
            p2 = p2*(n+1-i)
    return p2//p1

def fib(n):
        n=n%1000000007
        if n == 0:
            return (0, 1)
        else:
            a, b = fib(n // 2)
            c = a * (b * 2 - a)
            d = a * a + b * b
            if n % 2 == 0:
                return (c%1000000007, d%1000000007)
            else:
                return (d%1000000007, (c + d)%1000000007)
def fibonacci(n):
    a, b = fib(n)
    return a
k, l, r = map(int,input().split())
sum = 0
for n in range(l, r+1):
    sum = sum+choose(fibonacci(n+2),k%1000000007)

print(sum%1000000007)
    
