n = float(input("Please enter a number : "))

pf = 0
s = str(n)
l = len(s)

if l != 1:
    for a in range(-1,(l % 2)):
        if s[0 + a] != s[l - a]
            pf = 1
    
    if pf == 1:
        print(s , "is a Palindrome Number")
    else :
        print(s , "is not a Palindrome Number")      

else :
    print(s , "is a Palindrome Number")
