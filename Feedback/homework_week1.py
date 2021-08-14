"""
Grade: 95/100



TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""

# Note for Mehdi: I had help with this, as I struggled on my own
# ^ Which area did you have help with + how much? This is just to understand better if its okay
# ^ make sure for the future to still try independently! Feel free to ask Qs whenever you can to us as we're happy
# to answer anything, since we want the homeworks to be individual

class CashRegister:

    def __init__(self):

        self.total_items = None # {'item': 'price'}
        self.total_price = 0
        self.discount = 0


    def add_item(self, item, price):
        if self.total_items = None # <-- needs to be a double ==!
            # A single = in python means (x = y, set x to store the value of y)
            # Whereas a double == means (x == y, check if x has the same value as y).
            # = is for setting values, == is for comparisons!
            self.total_price = {}
        self.total_items.append[item] = price
        self.total_price += price

    def remove_item(self, item, price):
        self.total_items.pop(item)
        self.total_price -= price

    def apply_discount(self, total_discount):
        if self.total_price >= 100:
            self.discount = self.total_price * 0.1
            total_discount = self.total_price - self.discount
        print("You have qualified for a 10% discount! This has saved you: £{}".format(total_discount))

    def get_total(self):
        print("Your total bill is: £{}".format(self.total_items))

    def show_items(self):
        for item in self.total_items:
            print(item)

    def reset_register(self):
        self.total_items = None # {'item': 'price'}
        self.total_price = 0
        self.discount = 0


# EXAMPLE code run:

cher_ching = CashRegister()

# ADD

item1 = cher_ching.add_item('Hat', 14.99)
item2 = cher_ching.add_item('Sunglasses', 29.99)
item3 = cher_ching.add_item('Handbag', 49.99)
# item3 = cher_ching.add_item(['Handbag'] = 49.99)
# Do you need variables? add_item returns nothing, so you can just add as norm / nothing gets stored in those variables

cher_ching.get_total()
cher_ching.apply_discount()
cher_ching.show_items()
cher_ching.reset_register()
# ✓

"""
Great work
✓✓✓✓
"""

"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""

#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.mobile = mobile
        self.email = email
        self.subjects = dict()


class CFGStudent(Student):

    def add_subject(self, subject, grade):
        self.subjects[subject] = grade

    def remove_subject(self, subject):
        self.subjects.pop(subject)

    def view_all_subjects(self, subject):
        for subject in self.subjects:
            print(subject)

    def overall_mark(self, average_grade):
        received_marks = sum(self.subjects('grades'))
        total_marks = len(self.subjects('grades'))
        average_grade = received_marks / total_marks
        print("Overall Grade: {}".format(average_grade))


# Concrete student:
Nosheen = CFGStudent('Nosheen', 38, 4211, 07766226777, 'nosheen_masud@yahoo.com')

# Add subjects:
Nosheen.add_subject('Python Foundation', 60)
Nosheen.add_subject('SQL Foundation', 70)
Nosheen.add_subject('Software Track', 80)

# Overall Grade:
Nosheen.overall_mark()

"""
Task 2 is fantastic! Note that the methods implemented in the CFG Student can be moved to the Student class though - these
are still methods that are universal to all students (e.g. add subject), so you can just inherit them instead in the CFGStudent
class instead. This would mean less code repetition if you had multiple student sub-classes e.g. CFGStudent2, CFGStudent3, etc
Consider implementing the CFGStudent class with barely any methods in it - have it inherit most since many of these methods
are already universal anyway!
"""
