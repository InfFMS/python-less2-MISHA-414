n=int(input())
simple=[i for i in range(2, n)]
for i in range(n//2):
    a=simple[i]
    if a!=0:
        for i_nul in range(i+a, n//2, a):
            simple[i_nul]=0
answer=[]
for num in range((n-2)//2):
    if simple[num]!=0:
        answer.append(simple[num])
answer.append(n)
# answer=answer.append(n)
print(answer)
print(simple)