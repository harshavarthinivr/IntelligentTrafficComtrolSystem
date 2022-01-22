n=int(input("Enter number"))
k=0
for i in range(1,n+1):
 m=0
 for j in range(n,i,-1):
    print(end=" ")
 for k in range(1,i+1):
      print(k,end=" ")
 for m in range(i-1,0,-1):
      print(m,end=" ")
 print()
