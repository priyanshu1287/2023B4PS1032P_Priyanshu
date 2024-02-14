def second_largest(lis):   
    for i in range(lis.count(largest(lis))):
        lis.remove(largest(lis))
    print(largest(lis)) 

def largest(lis):
    largest=lis[0]
    for i in lis:
        if i>largest:
            largest=i 
    return largest

n=int(input("enter number of elements in the list: "))
l=[]
for i in range(n):
    a=int(input("enter number: "))
    l.append(a)

second_largest(l)
