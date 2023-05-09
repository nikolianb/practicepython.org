import random


def main():
    score = 0
    tries = 0
    inside_try = 0
    level = get_level()

    while (tries != 10):
        try:
            x,y = generate_integer(level) ##RANDOM NUMBER EVERYTIME THE FOR LOOP
            check_this = int(input(f"{x} + {y} = "))

            if(check_this != (x+y)):
                while (inside_try != 2 and check_this != (x+y)):
                    if(tries == 10):
                        break
                    print("EEE")
                    check_this = int(input(f"{x} + {y} = "))
                    inside_try +=1
                else:
                    print(f"{x} + {y} = {x+y}")
                    inside_try = 0
                    tries += 1
            else:
                tries +=1
                inside_try = 0
                score += 1
                continue
        except ValueError:
            continue
    else:
        print("Score: ",score)




def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if(level > 3 or level < 1):
                continue
            return level
        except ValueError:
            continue


def generate_integer(level):
    match level:
        case 1:
            x = random.randint(0,9)
            y = random.randint(0,9)
        case 2:
            x = random.randint(10,99)
            y = random.randint(10,99)
        case 3:
            x = random.randint(100,999)
            y = random.randint(100,999)
    return x,y

if __name__ == "__main__":
    main()