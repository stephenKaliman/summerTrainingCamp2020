def main():
    x1, y1, x2, y2 = map(int,input().split())
    return abs((x2-x1)*(y2-y1))+1

k = int(input())
for i in range(0,k):
    print(main())
