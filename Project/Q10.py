from random import randint as r

def app(x):
    for i in range(0,x):
        my_list.append(r(0,(99 * x)))

my_list = [r(20,50) , r(69,167) , r(5,55) , r(55,555)]

app(5)
my_list.append(69)

print(f"Original list : {my_list}")

my_list.pop(r(0,8))

print(f"Popped list : {my_list}")

my_list.remove(69)

print(f"Remove function list : {my_list}")

my_list.__delitem__(r(0,6))

print(f"Delete function list : {my_list}")