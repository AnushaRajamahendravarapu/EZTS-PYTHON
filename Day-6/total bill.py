#A shopping mall having 5% for men & 7% for women.
#individual discount for each item they purchase is 3*no.of items a customer purchase.
#calculate the total bill.
d={}
n=int(input("Enter no.of items: "))
for i in range(n):
    k=input("Enter item:")
    v=int(input("Enter item price:"))
    d[k]=v
l=[]
for i in d:
    l.append(d[i]-d[i]*(3*n)/100)
g=input("Enter gender:")
if g=="sale":
    bill=sum(l)-sum(l)*5/100
else:
    bill=sum(l)-sum(l)*7/100
j=0
print("items-prices:discount-prices")
for i in d:
    print(f"{i}-d{i}:{l[j]}")
    j+=1
else:
    print("*"*20)
print(f"Total bill: {bill}")
    


