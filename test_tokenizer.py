import unittest
from tokenizer import tokenize
import sys


class TestTokenizeMethods(unittest.TestCase):

    def test_tokenize(self):
        with open("test/test001.txt", "r") as f:
            src = f.read()
            self.assertEqual(src, "".join(tokenize(src)))


if __name__ == '__main__':
    unittest.main()
