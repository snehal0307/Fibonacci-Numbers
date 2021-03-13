nterms=13
n1,n2=0,1
count=0
while count<nterms:
    print(n1,end=",")
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count +=1
print(end="...")
