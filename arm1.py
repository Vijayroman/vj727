per,mov=map(int,input().split())
for i in range(per+1,mov):
  c=i
  fd=0
  while (i>0):
    r=i%10
    fd=fd+(r**3)
    i=i//10
    if(fd==c):
      print(fd,end=" ")
