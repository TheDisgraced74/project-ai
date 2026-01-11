from random import randint as r

a = r(1,99)
add = 0
my_list = []

for i in range(1,a):
    b = r(1,999)
    my_list.append(b)
    add += b

print(f"The list is {my_list}. \n Sum : {add}")
