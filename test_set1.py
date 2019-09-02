#!/usr/bin/env python

import unittest
import base64
import binascii

class TestSet1(unittest.TestCase):
    hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    target = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    def test_set1(self):
        hex_bytes = binascii.unhexlify(self.hex)
        # print(hex_bytes)
        # => "I'm killing your brain like a poisonous mushroom"

        b64_bytes = base64.b64encode(hex_bytes)
        # print(b64_bytes)
        # => b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

        self.assertEqual(self.target, b64_bytes.decode("ASCII"))

if __name__ == '__main__':
    unittest.main()
