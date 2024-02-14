def dictionary(lis_1,lis_2):
    d={}
    for i in range(n):
        d[lis_1[i]]=lis_2[i]
    print(d)

n=int(input("enter number of elements: "))
keys,values=[],[]

for i in range(n):
    a=input("enter key: ")
    keys.append(a)
    b=input("enter value: ")
    values.append(b)
    
dictionary(keys,values)
