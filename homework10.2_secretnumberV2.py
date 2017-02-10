import random

def set_secret_number(a):
    if a == 'e':
        secretNumber = random.randint(1,10)
        maxScore = 10
        maxRange = 10
        return [secretNumber, maxScore, maxRange]
    elif a == 'm':
        secretNumber = random.randint(1, 50)
        maxScore = 50
        maxRange = 50
        return [secretNumber, maxScore, maxRange]
    elif a == 'h':
        secretNumber = random.randint(1, 100)
        maxScore = 100
        maxRange = 100
        return [secretNumber, maxScore, maxRange]
    else:
        return False

def print_startscreen():
    print("\n################################################")
    print("###             W E L C O M E                ###")
    print("###                                          ###")
    print("### Please guess the secret number VERSION 2 ###")
    print("################################################\n")

def print_scorescreen(a):
    print("\n################################################")
    print("###  The secret number is between 1 and " + str(a) + "   ###")
    print("###            You have 10 tries             ###")
    print("################################################\n")

def print_jackpot(a,b):
    print("\n################################################")
    print("###               J A C K P O T              ###")
    print("###         The secret number was " + str(a) + "         ###")
    print("###             Your SCORE is " + str(b) + "             ###")
    print("################################################")

def print_gameover(a):
    print("\n################################################")
    print("###             G A M E   O V E R            ###")
    print("###               Too many trys              ###")
    print("###          The correct number was " + str(a) +"       ###")
    print("################################################")

def main():
    secret_list = []
    guess = None
    secret = None

    currentTry = 1
    maxTries = 10

    currentScore = None
    maxScore = None


    print_startscreen()

    while True:
        secret_list = set_secret_number(str(raw_input("Please set difficulty to (e)asy, (m)edium, (h)ard: ")).lower())

        if secret_list:
            secret = secret_list[0]
            currentScore = secret_list[1]
            maxScore = secret_list[2]

            print_scorescreen(maxScore)

            while guess != secret and currentTry <= maxTries:
                try:
                    guess = int(raw_input("Try " + str(currentTry) + "/10: "))

                    if guess == secret:
                        print_jackpot(secret,currentScore)
                        exit()
                    elif currentTry == maxTries:
                        print_gameover(secret)
                        exit()
                    else:
                        if guess < secret:
                            print("Higher")
                        elif guess > secret:
                            print("Lower")
                        currentTry += 1
                        currentScore -= (maxScore / 10)

                except ValueError:
                    print ("Please enter a number.")

if __name__ == "__main__":
    main()