a=int(input())
temp=a
sum=0
while(temp>0):
  x=temp%10
  sum+=x**3
  temp=temp//10
if(sum==a):
  print("yes")
else:
  print("no")
  
