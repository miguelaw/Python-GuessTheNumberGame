#Let's make sure we are using Python3 syntax 
#!/usr/bin/env python3

import random

#Number randomizer
randomNumber = random.randint(1,10)

#Set the number of tries to 0
tries = 0

#Start the game by setting win to False 
win = False

userName = input("Hello, what is your name? ")

print("Hello, ", userName + "!")

question = input("Would you like to play my game? [Y/N] ")
if question.lower() == "n":
    print("Ok, thanks anyways!")

# while the win is not true, run the while loop

else:
    print("Guess the random number! I'm thinking of a number between 1 & 10")
    while not win:
        try:
            guess = int(input("Your guess: "))

            if guess == randomNumber:
                print("You guessed correctly! The number was: ", guess)
                print("Number of tries: ", tries)
                win = True
            elif guess > randomNumber:
                print("Guess lower...")
                tries += 1
            elif guess < randomNumber:
                print("Guess higher...")
                tries += 1

        except ValueError:
            print ("Please Insert a valid value (only numbers allowed)")
            tries += 1

            
    
        

