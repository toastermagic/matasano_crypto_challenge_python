#!/usr/bin/env python

import sys
sys.path.append('../lib')

import unittest
from pprint import pprint
from single_byte_xor import *
from detect_single_character_xor import *
from results import *

class TestChallenge4(unittest.TestCase):
    data = open("data/4.txt", encoding="ISO-8859-1")
    target = "Now that the party is jumping\n"

    def test_challenge4(self):
        results = detect_single_character_xor(self.data)

        message_with_top_score = find_max(results, "score")

        self.assertEqual(self.target, message_with_top_score["message"])

if __name__ == '__main__':
    unittest.main()
