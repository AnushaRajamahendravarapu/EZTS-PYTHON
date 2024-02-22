#write a python program to check whether given number is prime or not
n=int(input())
for i in range(2,(n**0.5)+1):
    if n%i==0:
        print("not a prime")
        break
else:
    print("prime")
    
            
    
        
        
    

n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("prime")
else:
    print("not a prime")
    
            
        
            
        
