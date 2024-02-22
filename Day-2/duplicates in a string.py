#python program to remove duplicates in a string
str=input()
s1=""
for i in str:
    if i not in s1:
        s1+=i
print(s1)
