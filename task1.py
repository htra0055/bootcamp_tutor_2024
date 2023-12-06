
# python3 task1.py

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
list_num =[]
while num != "x":
    list_num.append(int(num))
    num = input("Please enter a number, press 'x' if finish: ")


'''
Block 2: Using a function to represent the digits in a form of a whole integer.
list_num is a list of input number, however, it is 'visualised' as a whole integer that being seprated by a comma
This block is using a loop that keep adding the value store in the index position of the list_num until it iterates the last element of list_num
Before being added, this value is times with the 10 with the power of the current len of the list (exp), exp will keep update 
'''
# Output the integer
output = 0
exp = len(list_num)-1

for index in range (0,len(list_num)):
    output += list_num[index]* (10 ** exp)
    exp -= 1

print(output)