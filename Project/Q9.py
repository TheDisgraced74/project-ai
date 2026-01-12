from random import randint as r

def main():
    my_list = [r(20,50) , r(69,167) , r(5,55) , r(55,555)]

    print(f"Original list : {my_list}")

    my_list.append(r(0,999))

    print(f"Appended list : {my_list}")

main()    