import math
def main():
        n= int(input())
        if(n%2==0):
            print(n//2, n//2, sep=' ')
            return        
        for m in range(3, int(math.sqrt(n))+1, 2):
           if(n%m==0):
               print(n//m, n*(m-1)//m, sep=' ')
               return
        print(1, n-1, sep=' ')


k = int(input())
for i in range(0,k):
        main()
