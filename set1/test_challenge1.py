#!/usr/bin/env python3
#
# 1. Convert hex to base64 and back.
#
# The string:
#
#   49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#
# should produce:
#
#   SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
#
# Now use this code everywhere for the rest of the exercises. Here's a
# simple rule of thumb:
#
#   Always operate on raw bytes, never on encoded strings. Only use hex
#   and base64 for pretty-printing.

import unittest
import base64
import binascii

class TestChallenge1(unittest.TestCase):
    hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    target = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    def test_challenge1(self):
        hex_bytes = binascii.unhexlify(self.hex)
        # print(hex_bytes)
        # => "I'm killing your brain like a poisonous mushroom"

        b64_bytes = base64.b64encode(hex_bytes)
        # print(b64_bytes)
        # => b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

        self.assertEqual(self.target, b64_bytes.decode("ASCII"))

if __name__ == '__main__':
    unittest.main()
