ui = int(input("Please enter the number : "))
d = 2

for o in range(0,ui):
    kill = ui // d
    if (ui % d) == 0 :
        print(f"{ui} is a composite number.")
        exit()
    
    if kill > d:
        print(f"{ui} is a prime number.")
        exit()

