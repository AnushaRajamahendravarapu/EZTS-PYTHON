#python program to print average of matrix
r,c=int(input("Rows: ")),int(input("Columns: "))
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
    for j in i:
        sum+=j
print(sum/(r*c))
