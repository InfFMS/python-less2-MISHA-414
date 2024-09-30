n=int(input())
simple=[i for i in range(2, n+1)]
for i in range(n-1):
    a=simple[i]
    count=0
    for k in range(i):
        if a%k!=0:
            simple
