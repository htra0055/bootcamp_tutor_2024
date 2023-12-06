

# python3 task2_ev.py

'''
Programming Task #2
Create a game where the user must correctly guess a randomly generated integer between 1 and 100.

The user should be notified whether their guess was “lower” or “higher” than the target number.

Note that you will need to use the random library’s randint function.

Remember:
- Use functions to group code
- Try to have functions that only do one “thing” (e.g. print a message, validate user input, check what message to display)
- Check for invalid inputs, notifying the user and re-prompting for a valid input
'''

import random

answer = random.randint(1,100)
#answer = 22


def check_input(guess):
    while not guess.isdigit() or int(guess) not in range(1, 101):
        print("Invalid Input! Your guess must be a number between 1 and 100:")
        guess = input("Please enter your guess again: ")
    return int(guess)


def check_guess(cur_guess):
    while cur_guess != answer:
        if cur_guess < answer:
            print("\n"+ "Your guess number is Lower than the Answer!")
        else:
            print("\n"+"Your guess number is Higher than the Answer!")
        cur_guess = check_input(input("You got this! Please enter your guess again: "))
    print("\n"+"---------------------------------------------"+ "\n"+"Congratulation! It is Correct!"+ "\n"+"--------------------------------------------")


current_guess = check_input(input("Please enter your first guess: "))
check_guess(current_guess)

print("Answer is", answer)