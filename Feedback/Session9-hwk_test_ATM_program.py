from unittest import TestCase
from ATM_program import verify_pin, log_in, run_atm

"""
Grade: 75% 

Only 3 out of 5 tests are actually running! I believe that the last 2 automatically evaluate to True because no code
is actually ran? So nothing actually evaluates to False and hence the tests runs pass-free. The cause of this is because
you are running your function verify_pin and passing Boolean as a parameter to it, so inside that function, it is running a
'True' == 1234 which evaluates to False, which subsequently causes the code in your testing function to never run. For future,
make sure to be careful around code nuances / place debug points to see if the code is fully running or not.

I do get what you were going for with the last 2 tests - slightly deducted marks, but I do get what your tests are going for hence
I thought to only slightly deduct marks if thats okay. This code overall is a brilliant submission as well, nicely done!
"""

class test_verify_pin(TestCase):

    def test_verify_pin(self):
        expected = True
        result = verify_pin('1234')
        self.assertEqual(expected, result)

class test_log_in(TestCase):

    def test_valid_pin(self):
        expected = True
        result = verify_pin('1234')
        self.assertEqual(expected, result)

    def test_invalid_pin(self):
        expected = False
        result = verify_pin('4211')
        self.assertEqual(expected, result)

class test_run_ATM(TestCase):

    def test_run_atm_value_error(self):
        if verify_pin(True): # <-- You're passing True to a function? The function is expecting pin?
            expected = ValueError
            result = run_atm(200)
            self.assertEqual(expected, result)
            # The 3 lines above are not executed at all! The verify_pin is returning False, because you are comparing
            # a boolean to the string '1234'! So the 3 above lines are never ran because the if condition statement
            # never evaluate to False

    def test_run_atm_correct_withdrawal(self):
        if verify_pin(True):
            expected = 50
            result = run_atm(50)
            self.assertEqual(expected, result)
            # Likewise for the three lines above as well!


# NOTES TO MYSELF:
# Previous code - where I went wrong
#
# class test_ATM_program(TestCase):
#
#     def test_verify_pin(self):
#         expected = True
#         result = verify_pin('1234')
#         self.assertEqual(expected, result)
#
#     def test_valid_pin(self):
#         expected = True
#         result = log_in(1234)
#         self.assertEqual(expected, result)
#
#     def test_invalid_pin(self):
#         expected = False
#         result = log_in(4211)
#         self.assertEqual(expected, result)
#
#     def test_run_atm_value_error(self):
#         expected = False
#         result = run_atm(200)
#         self.assertEqual(expected, result)
#
#     def test_run_atm_correct_withdrawal(self):
#         expected = True
#         result = run_atm(50)
#         self.assertEqual(expected, result)