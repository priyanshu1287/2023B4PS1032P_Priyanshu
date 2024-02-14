def dupl_remove(lis):
    for i in lis:
        if lis.count(i)>1:
            for j in range(lis.count(i)-1):
                lis.remove(i)
    print(lis)

list=[]
n=int(input("number of elements in list: "))
for i in range(n):
    a=input("enter number or string: ")
    list.append(a)

dupl_remove(list)
