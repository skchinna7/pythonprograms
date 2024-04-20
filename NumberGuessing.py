import random

guesses =[]
myComputer = random.randint(1,100)
player = int(input("Enter a number between 1-100: "))
guesses.append(player)

while player != myComputer:
    if player > myComputer:
        print("Too high!")
    else:
        print("Too low!")
    player = int(input("Enter a number between 1-100: "))
    guesses.append(player)   

else:
    print("You guessed it .Good job!")
    print("It took %i guesses. " % len(guesses))
    print("These are your guesses:")
    print(guesses)
