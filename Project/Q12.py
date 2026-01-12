uif = 1

def factorial(x,y):
    y = y * x
    if (x - 1) > 1:
        factorial(x - 1,y)
    if (x - 1) == 1:   
        print(f"{y} is the factorial of ", end = "")

ui = int(input("Please enter a number for factorial : "))

factorial(ui,uif)
print(ui)
