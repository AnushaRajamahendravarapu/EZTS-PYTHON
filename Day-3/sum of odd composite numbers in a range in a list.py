#python program to print sum of odd composite numbers in a range
def composite(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c>2:
        return 1
    else:
        return 0
n,m=map(int,input().split())
l=[]
for i in range(n,m+1):
    if i%2!=0:
        flag=composite(i)
        if flag==1:
            l.append(i)
print(sum(l))
print(l)

    
