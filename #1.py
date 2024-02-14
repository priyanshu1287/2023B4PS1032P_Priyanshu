def fibonacci_sequence(n):

    if n<0:
        print("enter a positive number")

    elif n==0:
        print("")

    elif n==1:
        print(0)

    else:
        a=0
        b=1
        print(a)
        print(b)    
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(c)
            
n=int(input("enter number of terms: "))
fibonacci_sequence(n)
