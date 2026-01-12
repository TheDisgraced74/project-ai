from random import randint as r

s = r(1,99)
g = 0
my_list = []

for i in range(1,s):
    ele = r(1,999)
    my_list.append(ele)

for o in my_list:
    if g < o :
        g = o

print(f"The list is {my_list}. \nThe greatest element in the list is {g}.")        
