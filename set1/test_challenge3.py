#!/usr/bin/env python

import sys
sys.path.append('lib')

import unittest
from pprint import pprint
from single_byte_xor import *

class TestChallenge3(unittest.TestCase):
    message = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    target = "Cooking MC's like a pound of bacon"

    def test_challenge2(self):
        message = max_score_message(score(self.message))["message"]

        self.assertEqual(self.target, message)

if __name__ == '__main__':
    unittest.main()
