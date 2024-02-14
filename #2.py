def most_vowels(n):
 
    lis_string=[]
    lis_count=[]
    vowel_lis=['a','e','i','o','u']

    print("enter the strings: ")
    for i in range(n):
        string=input()
        lis_string.append(string)

    for i in range(n):
        vowel=0
        for j in lis_string[i]:
            if j in vowel_lis:
                vowel+=1
        lis_count.append(vowel)

    a=max(lis_count)
    print("strings with most number of vowels:")
    for i in range(n):
        if lis_count[i] == a:
            print(lis_string[i])

n=int(input("enter number of strings: "))
most_vowels(n)
