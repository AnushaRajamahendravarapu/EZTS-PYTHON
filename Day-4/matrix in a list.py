#python program to print sum of the given matrix
r,c=int(input("Rows: ")),int(input("Columns: "))
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
print(l)
summ=0
for i in l:
    print(i)
    summ+=sum(i)
print(summ)
 
