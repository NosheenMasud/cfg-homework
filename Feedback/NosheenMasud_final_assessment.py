"""
Grade: 67.5 / 100
Amazing work as always Nosheen! Like your previous submissions you've given me wonderful answers that have blown me away
- fantastic work as before. It's been an absolute pleasure having you on the course as well & being able to mark your
work each week - you're beyond talented & I'm excited to see where you'll go! All the best for the future
"""

"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

Design a parent class called CFGStudent. It should have general attributes like name, surname,
age, email, student id and methods to fetch student’s full name and student’s id.
Important: there should be an option to pass student id when a new class object is generated,
HOWEVER, if no id is passed, then student_id should be automatically generated and assigned
to the class.
Design a child class called NanoStudent, which inherits from CFGStudent class. This class
should have exactly the same attributes as its parent class, as well as additional two called
‘specialization’ and ‘course grades’.
The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.
New methods ‘add_new_grade’ and ‘get_course_grades’ should be added. Please see the
skeleton structure in the final_assessment.py file. You can use it as a skeleton code for your
classes OR adjust it and create your own.
SEE ADDITIONAL COMMENTS in the file.

"""

# import random
#
# class CFGStudent:
#
#     def __init__(self, name, surname, age, email, student_id):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.email = email
#         self.student_id = student_id
#         # There could be instances where the student_id passed in is None!
#         # in those situations, you need to make sure you don't assign it (e.g. dont' do = student_id) and instead
#         # call the generate_id method to create a new ID instead
#
#     @staticmethod
#     def generate_id(): # This method is not used!
#         return str(random.randrange(1000, 10000))
#         'create a random new id, which is any number between 1,000 and 10,000'
#         'return id as a string'
#         "Example '8754' "
#
#     def get_id(self):
#         return self.student_id
#         'fetch student id'
#
#     def get_fullname(self):
#         return "Full name: {} {}".format(self.name, self.surname)
#         "Expected outcome should be 'Name Surname' "
#         'your code goes here'
#
#
# class NanoStudent(CFGStudent):
#
#     def __init__(self, name, surname, age, email, student_id, specialization, dict):
#         'your code goes here' # <--- you need to call the superclass's initiliaser too!
#         self.specialization = specialization
#         self.course_grades = dict() #or {}
#
#     @staticmethod
#     def generate_id():
#         return "NANO" + str(random.randrange(1000, 10000))
#         'create a random new id, which is a word NANO followed by any number between 1,000 and 10,000'
#         'return id as a string'
#         "Example 'NANO1234' "
#
#     def add_new_grade(self, subject, grade):
#         return self.course_grades[subject] = grade # <--- ??
#         # Why is this being returned
#         'update course_grades container'
#         "Example: pass in a task name and its grade, so that both are added to course_grades"
#
#     def get_course_grades(self):
#         return self.course_grades
#         'fetch course grades container and its values'

# 17/25

############################################

# Example run

# s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
# print(s.get_fullname())
# # returns 'Anna Smith'
# print(s.student_id)
# # returns '3868' or some other random number
#
# cfg_s = NanoStudent('Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
# print(cfg_s.get_fullname())
# # returns 'Mia Papandopulu'
# print(cfg_s.get_id())
# # returns 'NANO6180' or some other random number
#
# cfg_s.add_new_grade('theory', 95)
# cfg_s.add_new_grade('project', 78)
# print(cfg_s.get_course_grades())
# # returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""


##### TESTS ####



# def fib(n):
#
#     if n == 0:
#         return 0
#
#     if n == 1 or n == 2:
#         return 1
#
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# #print(fib(4))
#
# def even_fibonacci_sum(limit):
    # a = for num in range(limit): # <-- why is a set to equal a for loop?
    #     print(a)
    # even_fib = fib(a) % 2 == 0  # this may be pseudo code, to show you my thinking
    # return sum(even_fib)
    # Code doesn't work as it's not formatted correctly, but I think I get your thinking here
    # Basically, iterate through numbers up to the limit e.g. 1, 2, 3, ...., limit, and at each
    # number check if its even or not. I assume the next step is to sum up the even numbers (the sum method
    # would not work here tho as you would be calling it on a Boolean value! fib(a) % 2 == 0 returns True / False

# print(even_fibonacci_sum(limit=10))  # should be 44
# print(even_fibonacci_sum(limit=15))  # should be 188
# print(even_fibonacci_sum(limit=1))   # should be 0

# Mark: 18/25

# fib(1) = 1
# fib(2) = 1
# fib(3) = fib(2) + fib(1) = 1 + 1 = 2
# fib(4) = fib(3) + fib(2) = [fib(2) + fib(1)] + fib(2) = [1 + 1] + 1 = 3
#
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 

Given two non-empty arrays of integers, write a function that determines whether the second
array is a subsequence of the first one.
NOTE: A subsequence of an array in this case is a set of numbers that aren’t necessarily
adjacent in the array, but are in the same order as they appear in the array. Example:
● Array = [1,2,3,4]
● Numbers = [1,3,4] - valid subsequence
● Numbers = [2,4] - valid subsequence
● Numbers = [0,1,2,3,4] - invalid subsequence
● NB: a single number in an array and the array itself are both valid subsequences of the
array.
HINTS (only recommendations - feel free to follow your own algorithm):
1. You can solve this question by iterating through the main input array once.
2. Iterate through the main array and look for the first integer in the potential
subsequence. If you find that integer, keep on iterating, but now look for the second
integer. If you don’t find the first integer, is it worth continuing?
3. To actually implement what hint #2 describes you may want to declare a variable
holding your position in the potential sequence.
"""

def is_valid_subsequence(array, sequence):
    index = []
    for num in array:
        if num in array == num in sequence: # <-- unfortunately really confused by this
            index.append(num)
    return index # <-- keep getting returned a empty array for every test case?
    # I assume you're trying to check whether a number that exists in array also exists in sequence
    # however, there is no order-based checking (e.g. is the number in the correct place) - it seems that you move
    # forward towards this, but I don't believe it's fully accomplished unfortunately


#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE

# Mark: 12.5 / 25

"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)

Code review challenge: THIS IS A WRITTEN TASK NOT CODING.
Imagine that your colleague or a classmate asks you to review a
block of code (provided below) for them.
How can this code be improved? Is there anything missing or
maybe it needs to be refactored. Please write down your
recommendations for this review.



"""

# Single Responsibility Principle - class should hve only 1 thing to change
# open-closed - open for extention, closed for modification
# L - every sub class should be derived from parent class
# Interfaces - larger interfaces should be split into smaller ones
# Depenency principle - high level shuld not rely on low level....?  (Correct??)


"""
ANSWER:
1. the save_employee method should be an object instantiation, not a method - the way it is currently written, it goes against the single responsibility principle,
since there are too many things to change. It also appears to go against the Dependency principle and db.engine should not hold name, active_status, department and 
id within in. These should all be equal characteristics in the initialization of the class.
2. the remove_employee method also goes against the single responsibility method. You should either remove(delete) the entire instantiated object, or 1 piece of information 
from it per method, not 2, as is the case here. If you wanted to remove the whole instantiated object, then the name of the object would need to be called and a method to 
delete all of it.
3. the update_status method goes against the open-closed principle, as it is changing the existing code into something new, so modifying it rather than extending it
4. The print_employee_report method looks like it adheres to all the SOLID principles so seems to be written correctly. Using 'w' here to print the report is correct since 
printing the report would be a one off. If it was a case of adding to an existing file, then 'a' for append would need to be used as 'w' overwrites any existing files.
5. Within the class initialization, the following corrections need to be made:
    - self.active_status = active_status
    - self.id = id
6. It seems strange that parenthesis are used for the save_employee and remove_employee methods.
7. The update_department and update_status methods don't seem to be doing anything. 

"""

"""
20/25
Good answer!

To extend:
Consider exception handling! Some of these methods should ideally have a try/catch block since they are vulnerable / potential to raise
a error in the future and hence subsequently crash the program
Can you go in more depth on what SOLID / SRP are? break it down to like a 5-year old; why are they needed, what do they accomplish,
why should we even care for them, etc. You've already moved towards this beginning with Line 244, but if feasible deffo go into
more depth! So not how they acn be applied, but rather more depth into WHAT they are
"""