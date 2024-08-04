import random
import sys

number = random.randint(1,100)
print("I am thinking of a number between 1 and 100! You have 10 tries")

for guessTaken in range(1, 11):
    guess = int(input("Guess what number I'm thinking of! "))
    if guess == number:
        print("Correct! You guessed the number in "+ str(guessTaken) + " guesses!")
        sys.exit()
    elif guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")

print("Bummer! the number I was thinking of was " + str(number) +"")



