import random as rn

num = rn.randint(1,9)
tries = 0

while True:
    guess = input("Give me a number from 1 to 9: ")
    if(guess.lower() == "ext"):
        break
    guess = int(guess)
    if(guess > num):
        print("===To high, try again!===")
        tries += 1 
        continue
    elif(guess < num ):
        print("===Too low, try again! ===")
        tries += 1
        continue
    else:
        print("===" *5)
        print("RIGHT! THe number is ", num)
        break

if(num == guess):
    print("You guessed,",tries,"times")
    print("===" *5)
else:
    print("Thank you for playing, no worry you will get it right next time!")
