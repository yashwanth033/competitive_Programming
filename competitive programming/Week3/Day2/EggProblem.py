def broken(x):
    count=0
    k=14
    y=0
    while(y<x):
        z=y
        y=y+k
        k=k-1
        count=count+1
    if(x==y):
        return count
    count=count+(x-z)
    return count

for i in range(1,101):
    print(i,"-->",broken(i))
