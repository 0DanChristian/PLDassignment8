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

# play or exit
def play():
    lott = ' '*int(OFFSETT/2) + "             \033[2;33;46m🎉 Lottery 🎉\033[0m"
    design = (OFFSETT+len(lott))*'-'
    print ('{} \n{} \n{}'.format(design, lott, design))

# pick number
def pick():
    userInput = userNum()
    numWin = winningNo()
    lottery(userInput, numWin)

# call the rest of the function
def main():
    play()
    while True:

        # ask the user to play
        choice = input("\nDo you want to play? \033[3;37;40m(yes or no)\033[0m: ")
        if choice.replace(",","",10).title() == "Yes":

            # if yes, then the user will need to type 3 numbers
            string =  "\n               \033[2;33;46mPlease type your {}".format(num_Entry) + " lucky numbers!\033[0m"
            design = '\n'+ len(string) * "-"

            # display in this format
            print(design,
                    string,
                    design)

            pick()
            break
        # if the user doesnt want to play, then the program will exit
        elif choice.replace(",","",10).title() == "No":
            print("Thank you!\n")
            break
        
        # if the user input is invalid, such as: integers, this input accepts only y/n
        print("\nInvalid input\n")

