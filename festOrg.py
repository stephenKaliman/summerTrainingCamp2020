#most recent, I don't think I fixed it back after it started giving different numbers from before
import math
 
p = 1000000007
class phi:
    def __init__(self, a, b):#(a+b*sqrt(5)), in the form of phi
        self.a = a
        self.b = b
    def add(self, other):#(a1+b1*sqrt(5)) + (a2+b2*sqrt(5))
        res = phi(0,0)
        res.a = (self.a+other.a)%p
        res.b = (self.b+other.b)%p
        return res
    def sub(self, other):#(a1+b1*sqrt(5))-(a2+b2*sqrt(5))
        res = phi(0,0)
        res.a = (self.a-other.a)%p
        res.b = (self.b-other.b)%p
        return res
    def mult(self, other):#(a1+b1*sqrt(5))*(a2+b2*sqrt(5))
        res = phi(0,0)
        res.a = (self.a*other.a + 5*self.b*other.b)%p
        res.b = (self.b*other.a + self.a*other.b)%p
        return res
    def div(self, other):#(a1+b1*sqrt(5))/(a2+b2*sqrt(5))
        res=phi(0,0)
        res.a = (self.a*other.a - 5*self.b*other.b)*inv(other.a*other.a-5*other.b*other.b)%p
        res.b = (self.b*other.a - self.a*other.b)*inv(other.a*other.a-5*other.b*other.b)%p
        return res
    def pwr(self, exp): 
        res = one
        k = 0
        while(exp>>k):
            k+=1
        while(k>=0):
            res = res.mult(res)
            if((exp>>k)&1):
                res = res.mult(self)
            k-=1
        return res
    def __str__(self): #toString, for debugging
        return str(self.a)+' '+str(self.b)
def inv(k): #k^(-1) (mod p)
    return pow(k,p-2,p)
one = phi(1,0) #just 1
phiplus = phi(inv(2),inv(2)) #(1+sqrt(5))/2 (mod p)
phiminus = phi(inv(2),p-inv(2)) #(1-sqrt(5))/2 (mod p)
def binom(n,k):#basic binomial coefficient
    p1 = 1
    p2 = 1
    if(n<k):
        return 0
    if(k<n//2):
        for i in range(1,k+1):
            p1 = p1*i%p
            p2 = p2*(n+1-i)%p
    else:
        for i in range(1,n-k+1):
            p1 = p1*i%p
            p2 = p2*(n+1-i)%p
    return p2*inv(p1)%p
def stirlingCoeff(k):#coefficients of the expansion x(x-1)(x-2)(x-3)***(x-k+1) for numerator of the binomial coefficient
    coeffs = [1]
    for n in range(1,k):
        coeffs.append(0)
        for m in range(n,0,-1):
            coeffs[m] = (coeffs[m]-n*coeffs[m-1])%p
    return coeffs
def fibsum(m, k):#sum of first m fibonacci numbers to the kth power, using binets formula and partial geometric series formula
    sum = 0
    if(k%2==0):
        for i in range(0,k+1):
                diff = (phiplus.pwr((m+1)*(k-i)).mult(phiminus.pwr((m+1)*(i))).sub(one)).mult(phi(pow(-1,i)*binom(k,i),0)).div(phiplus.pwr(k-i).mult(phiminus.pwr(i)).sub(one))
                if(i==k/2 and i%2==0): diff = phi(m+1,0).mult(phi(binom(k,k//2),0))
                sum = (sum+diff.a)%p
        sum = sum*pow(inv(5),k//2,p)%p
    else:
        for i in range(0,k+1):
                diff = (phiplus.pwr((m+1)*(k-i)).mult(phiminus.pwr((m+1)*(i))).sub(one)).mult(phi(pow(-1,i)*binom(k,i),0)).div(phiplus.pwr(k-i).mult(phiminus.pwr(i)).sub(one))
                if(i==k/2 and i%2==0): diff = phi(m+1,0).mult(phi(binom(k,k//2),0))
                sum = (sum+diff.b)%p
        sum = sum*pow(inv(5),(k-1)//2,p)%p   
    return sum
def main():
    fibsums = []
    factorialDenom = 1
    ans = 0
    k,l,r = map(int,input().split())
    for m in range(k,0,-1):
        fibsums.append(fibsum(r+2,m)-fibsum(l+1,m))
        factorialDenom = factorialDenom*inv(m)%p
    coeffs = stirlingCoeff(k)
    for i in range(0,k):
        ans = (ans+ coeffs[i]*fibsums[i])%p
    ans = ans*factorialDenom%p
    print(ans)
main()
