n,x=map(int,input().split(" "))
if (x*n%4)==0:
  print(x*n//4)
else:
  print((x*n//4)+1)
