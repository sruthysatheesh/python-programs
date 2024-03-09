i,sum=1,0
n=int(input("Enter the limit:"))
if n<0:
  n=int(input("enter a valid limit:"))
while i<=n:
    sum+=i
    i+=1
print("sum of", n , "natural numbers =", sum)
