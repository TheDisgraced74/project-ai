import sys

def check(x,y):
    if x == y:
        sys.exit(0)

l = int(input("Please enter the length of series desired : "))

t1 = 0
t2 = 1
p = 0

for i in range(0,((l // 2) + 1)):
    print(t1 , "," , end = " ")
    p += 1
    check(p,l)
    print(t2 , "," , end = " ")
    p += 1
    check(p,l)
    t1 = t1 + t2
    t2 = t1 + t2    

