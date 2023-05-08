import random 

pname1 = input("What's your name? ")
#pname2 = input("And whats your name? ")
kompjuteri = ["rock", "paper", "scissors"]
player_score = 0 
pc_score = 0

while True:
    if(player_score != 0 or pc_score != 0):
            print("===========")
            print(f"{pname1}:",player_score,"Computer:", pc_score)
            print("===========")
    play1 = input(f"{pname1}:\nRock/Paper/Scissors: ").lower()
    if(str(play1).strip() == "quit"):
        print("****GAME OVER*****")
        break
    play2 = str(random.choice(kompjuteri))
    
    print("PC: ",play2)


    if(play1 == play2):
        print("===" *5)
        print("Even")
        print("===" *5)
        continue
    elif(play1 == "rock"): #ROCK BEATS SCISSORS
        if(play2 == "scissors"):
            print("===" *5)
            print(f"{pname1} won!")
            print("===" *5)
            player_score += 1
            continue
        else:
            print("===" *5)
            print("PC won!")
            print("===" *5)
            pc_score += 1
            continue
    elif(play1 == "scissors"): #SCISSORS BEATS PAPER
        if(play2 == "paper"):
            print("===" *5)
            print(f"{pname1} won!")
            print("===" *5)
            player_score += 1 
            continue
        else:
            print("===" *5)
            print("PC won!")
            print("===" *5)
            pc_score += 1
            continue

    elif(play1 == "paper"): #PAPER BEATS ROCK
        if(play2 == "rock"):
            print("===" *5)
            print(f"{pname1} won!")
            print("===" *5)
            player_score += 1 
            continue
        else:
            print("===" *5)
            print("PC Won!")
            print("===" *5)
            pc_score += 1
            continue
    

