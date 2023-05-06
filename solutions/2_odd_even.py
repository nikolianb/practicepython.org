number = int(input("What is the number you want to check? \n"))
check = int(input("Give me  a number to divide by: \n"))

if(number % 4 == 0):
    print("The number is a muliplie of 4")
elif(number % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")


if(number % check == 0):
    print(number, "does divide even by ", check)
else:
    print(number, "does not divide even by", check)