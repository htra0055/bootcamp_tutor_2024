
# python3 task2.py

'''
Programming Task #2
Create a game where the user must correctly guess a randomly generated integer between 1 and 100.
The user should be notified whether their guess was “lower” or “higher” than the target number.
'''

import random

answer = random.randint(1,100)
#answer = 22

'''
this function validate user input by printing error message if input is not a digit or in range [1,101]
parameter: guess = input of the user
return: integer of guess
'''
def check_input(guess):
    while not guess.isdigit() or int(guess) not in range(1, 101):
        print("Invalid Input! Your guess must be a number between 1 and 100:")
        guess = input("Please enter your guess again: ")
    return int(guess)


'''
this function notifies the user whether their guess was “lower” or “higher” than the target number or correct
parameter: cur_guess = an integer
return: a string statement
'''
def check_guess(cur_guess):
    while cur_guess != answer:
        if cur_guess < answer:
            print("\n"+ "Your guess number is Lower than the Answer!")
        else:
            print("\n"+"Your guess number is Higher than the Answer!")
        cur_guess = check_input(input("You got this! Please enter your guess again: "))
    print("\n"+"---------------------------------"+ "\n"+"Congratulation! It is Correct!"+ "\n"+"---------------------------------")



current_guess = check_input(input("Please enter your first guess: ")) # pass input() of the user in check_input function and assign the return value into current_guess variable
check_guess(current_guess) # notify the user of the status of their guess

print("Answer is", answer)