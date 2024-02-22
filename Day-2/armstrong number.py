#python program to check whether given number is armstrong number or not
n=int(input())
sum=n
rev=0
while n>0:
    digit=n%10
    rev=rev+digit**3
    n//=10
if rev==sum:
    print("armstrong number")
else:
    print("not a armstrong number")
