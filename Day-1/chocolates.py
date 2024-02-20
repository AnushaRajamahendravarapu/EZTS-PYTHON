n,x=map(int,input().split(" "))
t=n-x
if x>=n:
    print(n=0)
else:
    t=n-x
    if t%4==0:
        n=t//4
    else:
        n=(t//4+1)
print(n)
