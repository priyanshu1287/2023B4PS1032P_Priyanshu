#pattern 1
n=5
for i in range(n+1):
    for j in range(n-i):
        print("   ",end="")
    for k in range(i):
        print(k+1," ",end="")
    print("\n")

print("\n\n")

#pattern 2
for i in range(n): 
    print((n-i)*" ",end="")
    print(((2*(i))+1)*"*"," ",end="")
    print("")
for i in range(n): 
    print((i+1)*" ",end="")
    print(((2*(n-i-1))+1)*"*"," ",end="")
    print("")
