# Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

# introduction
print("\n\033[1;37;45mWelcome!\033[0m\n")
# ask for user
user = input("\nPlease enter your \033[1mname\033[0m: ")
# welcome
print(f"\n\033[7;34;40mWelcome {user}!, this program is a guess game!\033[0m \n")

# import
import random
import sys

# define var
def guess():
    number = random.randint(1,100)
    count  = 1
    guess  = int(input("Enter your guess between \033[4;37;40m1 and 100\033[0m: "))

    while guess != number:
        count   += 1
        if guess > (number + 10):
            print("\nIt's quite high!")
        elif guess < (number - 10):
            print("\nThat is quite too low!")
        elif guess > (number + 5):
            print("\nYou're close, lower it a little bit")
        elif guess < (number -5):
            print("\nYou're close, push it up a little bit")
        elif guess > number:
            print("\nA little bit high, but you're almost there!")
        elif guess < number:
            print("\nA little bit low, you're almost there!")

        guess = int(input("\033[3;31;40m\nTry again \033[0m"))

