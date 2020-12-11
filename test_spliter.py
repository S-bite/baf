import unittest
from tokenizer import tokenize
from spliter import *

import sys


class TestSplitMethods(unittest.TestCase):
    def test_get_next_nonspace_token(self):
        src = "a = /* @ 1, 2, 3 * /"
        tokens = tokenize(src)
        self.assertEqual(get_next_nonspace_token(tokens, 0), ("=", 2))
        self.assertEqual(get_next_nonspace_token(tokens, 1), ("=", 2))
        self.assertEqual(get_next_nonspace_token(tokens, 2), ("/*", 4))

    def test_next_tokens_are_annotation(self):
        print("?")
        src = "a = /* @ 1, 2, 3 * /"
        tokens = tokenize(src)
        self.assertEqual(next_tokens_are_annotation(tokens, 0), False)
        self.assertEqual(next_tokens_are_annotation(tokens, 1), False)
        self.assertEqual(next_tokens_are_annotation(tokens, 2), False)
        self.assertEqual(next_tokens_are_annotation(tokens, 3), True)
        self.assertEqual(next_tokens_are_annotation(tokens, 4), False)

    def test_make_choosable_tokens(self):
        src = "a = /* @ 1, 2, 3 * /"
        tokens = tokenize(src)
        choosable_tokens = make_choosable_tokens(tokens)
        print(choosable_tokens)
        self.assertEqual(choosable_tokens, ["a", ["1", "2", "3"]])


if __name__ == '__main__':
    unittest.main()
