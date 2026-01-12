age = float(input("This program tells if you are eligible for vot right now or not.\nPlease enter your age : "))

if age <= 0 :
    print("Invalid input")

elif age <= 18 :
    print(f"You are not eligible for voting.\nYou will be in {(18 - age) * 31622400000000} microseconds.")

elif age <= 110 :
    print("You are eligible for voting.")

else :
    print("Invalid input")