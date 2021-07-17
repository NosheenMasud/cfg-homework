### Note for Mehdi: we weren't set the correct homework, the below was given to us as homework,
# and then a script was given to us for the actual homework to be able to do the unit testing homework ###

# Write a function that can read contents of a file and can handle cases when provided file name does not exist:
# Handle Error cases gracefully displaying an informative message to the user.
# What Error type can we use here?  (check Python documentation)

"""
Grade: 95 / 100

- Grading you by this homework - apologies it took me so long to understand (was confused for a sec about exercise vs homework?)
- So there's no mark scheme, so I'm marking you here against:
-   1) Demonstration of Exception Handling
-   2) General code quality
-   3) Input / Output mechanism

- Criteria 1: Good exception handling approach! You act prudent and put some good resilient code around the program
Consider where the exception handling should be done though - e.g. around places that are most likely to throw errors
/ may be vulnerable, instead of string == string comparions (because you can place a print statement htere and not do
a file.read()?).
32 / 33

- Criteria 2: Excellent quality code! Variables are named well and everything is structured reasonably.
30 / 34
Make your code dynamic / agnostic though of your own environment! So static, hard-typed file paths make the program useless
on other computers; it's better to have programs that are transferrable / work on multiple machines

- Criteria 3: All good here as well - you do a check against the input (to make sure its expected),
and output appropriately as well
33/33
"""

name = input("what is the name of the file you would like to read? ")
file_name = "todo.txt"

def readFile(name):
    try:
        if name != file_name: # <-- good use of error handling! Is error handlnig needed fully here though?
            # A print statemnet would just as much suffice - a FileNotFoundError may be more appropriate around line 29
            # (since that's where the error is most likely to occur) instead of the part that checks file names (since
            # you're just doing string comparisons).
            raise FileNotFoundError

        file = open('C:\\Users\\noshe\\NanoPythonFoundation\\Session_5_6\\todo.txt', 'r')
        # ^ For file path, this may not be useful in the future if it's hard typed - try making the file path relative?
        # For example - this file path may work on your computer, but as soon as its transferred elsewhere it can cause
        # issues as it's hard-typed directly for your own environment. Making a file path relative (e.g. find todo.txt
        # based on where you are at that moment) is often better (for users; as your program is agnostic regardless
        # of the environment it's based in).

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