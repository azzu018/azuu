y=list(input())
k=0
while(k<len(y)):
    temp=y[k]
    y[k]=y[k+1]
    y[k+1]=temp
    k+=2
print("".join(y))
