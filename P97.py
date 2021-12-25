import random
num=int(random.randint(0,9))

numGuess=int(input("Guess what number I'm thinking of:"))

while not numGuess == num :
    if numGuess==num :
        print("Nice job, you guessed right my number was ",num)
    elif numGuess<num :
        print("You guessed too low, try again")
    elif numGuess>num :
        print("You guessed to high, try again")
    
    numGuess = int(input("Guess what number I'm thinking of:"))

if numGuess==num :
        print("Nice job, you guessed right my number was ",num)