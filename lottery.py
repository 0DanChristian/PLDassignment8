# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

# introduction
print("\n\033[1;37;45mWelcome!\033[0m\n")
# ask for user
user = input("\nPlease enter your \033[1mname\033[0m: ")
# welcome
print(f"\n\033[7;34;40mWelcome {user}!, this is a lottery program\033[0m \n")

# import
import random

# var
num_Entry = 3
min_no = 0
max_no = 9
OFFSETT = 4

# win or lose in the program

def lottery(userInput, numWin):
    if userInput == numWin:
        # if the user won
        print (f"\nCongratulations! You won a peso! ",
                "\nYour numbers: ", userInput,
                "\nThe winning numbers are: ", numWin, "\n")
    else:
        # if the user lose
        print ("\n\033[3;31;40mUnfortunately, you lose\033[0m😢",
                "\nYour numbers: ", userInput,
                "\n\033[1;32;40mThe winning numbers are\033[0m: ", numWin, "\n")

# let us get the numbers that the user wants
def userNum():
    userInput = []
    while len(userInput) < num_Entry:
        # pick a number
        nos = (input("Pick a number from \033[4;37;40m{} to {}\033[0m: ". format(min_no, max_no)))
        try:
            nos = int(nos)
        except:
            # the program will error if the input is not an integer
            print("You must input an integer")
            continue
        if min_no <= nos <= max_no:
            if nos not in userInput:
                userInput.append(nos)
            else:
                # your number cannot be picked twice
                print("Numbers cannot be picked twice")
        else:
            # if the user input is above the range
            print("The range is only 0-9")
    
    # the program will naturally sort the numbers
    return sorted(userInput)

# list of winning random nos ranging from 0-9 with a range of 3 values
def winningNo():
    return sorted(random.sample(range(min_no, max_no),num_Entry))

