#!/usr/bin/env python

import sys
sys.path.append('../lib')

import unittest
from binascii import hexlify
from pprint import pprint
from xor import *
from break_repeating_xor_key import *
from detect_single_character_xor import *
from results import *

class TestChallenge6(unittest.TestCase):
    with open("data/6.txt", encoding="ISO-8859-1") as file:
        data = file.read()

    encrypted_bytes = b64decode(data)

    def test_hamming_distance(self):
        self.assertEqual(hamming_distance(b"this is a test", b"wokka wokka!!!"), 37)

    def test_minimum_hamming_distances(self):
        # NOTE: could potentially calculate hamming distance range from cipher text length..
        results = minimum_hamming_distances(self.encrypted_bytes, range(2,41))

        self.assertEqual(find_min(results, "normalized_hamming_distance")["keysize"], 29)

    def test_transpose(self):
        bytes = "abcdefghijkl"
        target = [['a', 'd', 'g', 'j'], ['b', 'e', 'h', 'k'], ['c', 'f', 'i', 'l']]

        self.assertEqual(transpose(bytes, 3), target)

    def test_challenge6(self):
        # number of bytes: 2871
        # block size: 29
        # number of blocks: 99
        # padding: 24 

        # block size calculated by prior hamming distance test..
        blocks = transpose(self.encrypted_bytes, 29)

        collection = []

        for block in blocks:
            # FIXME: score() should take bytes not hex
            collection.append(find_max(score(hexlify(bytes(block))), "score"))

        key = ""
        for data in collection:
            key += data["key"]

        decrypted_message = repeating_xor(self.encrypted_bytes, key.encode("ASCII"))

        with open("data/6-decrypted.txt", encoding="ISO-8859-1") as file:
            target = file.read()

        self.assertEqual(decrypted_message.decode("ASCII"), target)

if __name__ == '__main__':
    unittest.main()
