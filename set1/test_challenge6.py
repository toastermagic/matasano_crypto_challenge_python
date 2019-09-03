#!/usr/bin/env python

import sys
sys.path.append('lib')

import unittest
from binascii import hexlify
from pprint import pprint
from xor import *
from break_repeating_xor_key import *
from results import *

class TestChallenge6(unittest.TestCase):
    data = open("data/6.txt", encoding="ISO-8859-1").read()

    def test_hamming_distance(self):
        self.assertEqual(hamming_distance(b"this is a test", b"wokka wokka!!!"), 37)

    def test_minimum_hamming_distance(self):
        doc = b64decode(self.data)

        results = minimum_hamming_distances(doc, range(2,41))
        pprint(sort(results, "normalized_hamming_distance"))

        self.assertEqual(find_min(results, "normalized_hamming_distance")["keysize"], 29)

    def test_challenge6(self):
        True

if __name__ == '__main__':
    unittest.main()
