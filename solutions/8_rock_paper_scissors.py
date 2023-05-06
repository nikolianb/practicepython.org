import random 

pname1 = input("What's your name? ")
#pname2 = input("And whats your name? ")
kompjuteri = ["rock", "paper", "scissors"]

while True:
    play1 = input(f"{pname1}:\nRock/Paper/Scissors: ").lower()
    play2 = str(random.choice(kompjuteri))
    print("PC: ",play2)


    if(play1 == play2):
        print("===" *5)
        print("Even")
        print("===" *5)
    elif(play1 == "rock"): #ROCK BEATS SCISSORS
        if(play2 == "scissors"):
            print("===" *5)
            print(f"{pname1} won!")
            print("===" *5)
        else:
            print("===" *5)
            print("PC won!")
            print("===" *5)
    elif(play1 == "scissors"): #SCISSORS BEATS PAPER
        if(play2 == "paper"):
            print("===" *5)
            print(f"{pname1} won!")
            print("===" *5)
        else:
            print("===" *5)
            print("PC won!")
            print("===" *5)
    elif(play1 == "paper"): #PAPER BEATS ROCK
        if(play2 == "rock"):
            print("===" *5)
            print(f"{pname1} won!")
            print("===" *5)
        else:
            print("===" *5)
            print("PC Won!")
            print("===" *5)
    continue