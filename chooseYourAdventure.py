#########################################################################
# Date Created: 03/30/2024                                              #
# Name of Project: Choose you Adventure!                                #
# Conceptes Used: If/Else conditions, Variables, Data Types, Operators, #
#                 Elif condition, Lists.                                #
#########################################################################

name = input("Please type your name: ")
print("\n-------------------------------------------------------------------")
print(f"  Hello, {name} and welcome to the Adventerous game of THE JUNGLE!")
print("-------------------------------------------------------------------\n")

print("You are driving to your home, while all of the sudden your car broke down.")
answer = input("You have two ways to go, (left/right)? ").lower()

if answer == "left":
    answer = input("You have chose left, and find a path with three trees to the left and a swamp to the right. Which way would you like to go? (trees/swamp) ").lower()
    if answer == "trees":
        print("The trees are haunted and have made you lost forever. You Lose!")
    elif answer == "swamp":
        answer = input("The swamp looks a bit dangerous. Would you like to swim across or walk around it? (swim/walk) ").lower()
        if answer == "swim":
            print("You have tried to swim across it but the pirhanas in there were hungry. You lose!")
        elif answer == "walk":
            print("Okay good, you managed to find a road and find someone to help! You win!")            
        else:
            print("Sorry not a valid answer, you lose!")
    else:
        print("Sorry not a valid answer, you lose!")

elif answer == "right":
    answer = input("You chose right, you see lots of wolves on the left and some bears on the right. Which way do you want to go? (right/left) ").lower()
    if answer == "left":
        print("Oh come on, they're wolves did you expect not to eat you? You Lose!")
    elif answer == "right":
        answer = input("Okay this might be unfair but the bears are sleeping. Want to tame them or run for your life? (tame/run) ").lower()
        if answer == "tame":
            print("Really? Why even explain this. You Lose!")
        elif answer == "run":
            print("Wow you can run really fast! but not as fast as the tiger behind you. You Lose!")
        else:
            print("Sorry not a valid answer, you lose!")
    else:
        print("Sorry not a valid answer, you lose!")

else:
    print("Sorry not a valid answer, you lose!")