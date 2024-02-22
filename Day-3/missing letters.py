s,s1=map(str,input().split(" "))
s2=""
for i in s1:
    if i not in s:
        s2+=i
print(s2)
