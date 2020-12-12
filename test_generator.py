import unittest
from tokenizer import tokenize
from spliter import make_choosable_tokens
from generator import *


import sys


class TestGenerateMethods(unittest.TestCase):
    def test_generate_every_possible_code(self):
        src = "a = 3 /* @ 1, 2, 3 */"
        possible_codes = generate_every_possible_code(
            make_choosable_tokens(tokenize(src)))
        self.assertEqual(possible_codes, ["a = 1", "a = 2", "a = 3"])
        src = "a = 3 /* @ 1, 2, 3 */0/* @ 1, 2, 3 */"
        possible_codes = generate_every_possible_code(
            make_choosable_tokens(tokenize(src)))
        self.assertEqual(possible_codes, [
                         "a = 11", "a = 12", "a = 13", "a = 21", "a = 22", "a = 23", "a = 31", "a = 32", "a = 33"])


if __name__ == '__main__':
    unittest.main()
