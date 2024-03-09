i=1
sum=0
n=int(input("Enter the limit:"))
if n<0:
  print("enter a valid limit:")
else:
  while i<=n:
    sum+=i
    i+=1
  printf("sum of", n , "natural numnbers=", sum)
