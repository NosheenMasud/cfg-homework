### Q4.	Write tests for the newly created Palindrome function. Provide a brief explanation for your test case options.

from unittest import TestCase, mock
from assessment_2 import is_Palindrome

class Test_isPalindrome:

    def test_even_word(self):
        expected = 0
        result = 'tabbat'
        self.assertEqual(expected, result)

    def test_is_eqial_to(self):
        expected = True
        result = left_index == right_index('tabbat')
        self.assertEqual(expected, result)


# and then run in terminal to see if tests come back as passed or failed

"""
Mark: 3 / 8
 
The tests are failing? They are not able to run correctly as teh code itself within the is_Palindrome function is not
executible (e.g. left_index = # text)

Tests are written out well though - however, they are confusing? You do not call the is_Palindrome function at all
in the tests - in this instance, how is the is_palindrome method being tested if it's never called?

The actual structure is correct, but the function itself is actually never being tested at all - moreover, line 9 expects
0 but the function doesn't return any value at all? It is set-up to print output instead
"""