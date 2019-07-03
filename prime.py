s,m=map(int,input().split())
for tap in range(s+1,m,1):
    if(tap>1):
        for v in range(2,tap):
            if(tap%v==0):
                break
        else:
            print(tap,end=" ")
