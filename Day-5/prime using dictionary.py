def isprime(m):
    for i in range(2,m):
        if m%i==0:
            return "Composite"
    else:
        return "Prime"
n=int(input())
d={}
for i in range(n):
    k=i+1
    v=isprime(i)
    d[k]=v
print(d)
