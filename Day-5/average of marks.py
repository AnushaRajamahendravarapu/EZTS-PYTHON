#python program to print average of student marks data base using nested dictionary
n=int(input("Enter no.of students: "))
m=int(input("Enter no.of subjects: "))
d={}
for i in range(n):
    k=input("Enter rollno:")
    v={}
    for j in range(m):
        sub=input("Enter Subject name: ")
        marks=int(input("Enter marks: "))
        v[sub]=marks
    d[k]=v
for i in d:
    l=list(d[i].values())
    print(f"{i}:{sum(l)/m}")
