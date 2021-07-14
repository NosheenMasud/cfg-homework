### Note for Mehdi: we weren't set the correct homework, the below was given to us as homework,
# and then a script was given to us for the actual homework to be able to do the unit testing homework ###

# Write a function that can read contents of a file and can handle cases when provided file name does not exist:
# Handle Error cases gracefully displaying an informative message to the user.
# What Error type can we use here?  (check Python documentation)

name = input("what is the name of the file you would like to read? ")
file_name = "todo.txt"

def readFile(name):
    try:
        if name != file_name:
            raise FileNotFoundError

        file = open('C:\\Users\\noshe\\NanoPythonFoundation\\Session_5_6\\todo.txt', 'r')
        content = file.readlines()
        print(content)
        file.close()

    except:
        print("This file cannot be recognised")

readFile(name)




### Actual Homework ###
#
# Simple ATM program
#
# Using exception handling code blocks such as try/ except / else / finally (NB: the more the better, but try to use at least two key words
# e.g. try/except) write a program that simulates and ATM machine to withdraw money.
# Tasks:
# 1.	Prompt user for a pin code
# 2.	If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again.
#       You can give a user a maximum of 3 attempts and then exit a program.
# 3.	Set account balance to 100.
# 4.	Now we need to simulate cash withdrawal
# 5.	Accept the withdrawal amount
# 6.	Subtract the amount from the account balance and display the remaining balance (NOTE! The balance cannot be negative!)
# 7.	However, when a user asks to ‘withdraw’ more money than they have on their account, then you need to
# raise an error an exit the program.
#
# find_pin = int(input("Welcome. Please enter your pin number: "))
# pin_no = 4211
#
# def get_pin_number(find_pin):
#     try:
#         if find_pin != pin_no:
#             raise Exception
#         print("Your account balance is £100")
#
#     except:
#         print("The pin number is incorrect, please try again")


