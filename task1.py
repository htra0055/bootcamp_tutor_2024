
# python3 task1_ev.py

'''
Programming Task #1
Given a list of digits, determine the integer that it represents.
This program has two block of code:
Block 1: Create a list of digits
Block 2: Output an integer that it represents.
'''


'''
Block 1: A loop keep asking for number until user press 'x', these numbers are the put in a list
'''
num = input("Please enter a number, press 'x' if finish: ")
lst_num =[]
while num != "x":
    lst_num.append(int(num))
    num = input("Please enter a number, press 'x' if finish: ")


'''
Block 2: Using a function to represent the digits in a form of a whole integer.
'''
# Output the integer
output = 0
exp = len(lst_num)-1

for index in range (0,len(lst_num)):
    output += lst_num[index]* (10 ** exp)
    exp -= 1

print(output)