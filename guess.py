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

