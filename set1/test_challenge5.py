#!/usr/bin/env python

import unittest
from binascii import hexlify
from helpers import *
from pprint import pprint

class TestChallenge5(unittest.TestCase):
    message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

    target = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

    def test_challenge5(self):
        hex = hexlify(repeating_xor(self.message.encode("ASCII"), "ICE".encode("ASCII"))).decode("ASCII")

        self.assertEqual(self.target, hex)

if __name__ == '__main__':
    unittest.main()
