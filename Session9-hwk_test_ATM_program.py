from unittest import TestCase
from ATM_program import verify_pin, log_in, run_atm


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
        if verify_pin(True):
            expected = ValueError
            result = run_atm(200)
            self.assertEqual(expected, result)

    def test_run_atm_correct_withdrawal(self):
        if verify_pin(True):
            expected = 50
            result = run_atm(50)
            self.assertEqual(expected, result)


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