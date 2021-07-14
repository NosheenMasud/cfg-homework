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