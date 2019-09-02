#!/usr/bin/env python

import unittest
from helpers import *

class TestSet2(unittest.TestCase):
    buf_x = "1c0111001f010100061a024b53535009181c"
    buf_y = "686974207468652062756c6c277320657965"

    target = "746865206b696420646f6e277420706c6179"

    buf_x_bytes = binascii.unhexlify(buf_x)
    buf_y_bytes = binascii.unhexlify(buf_y)


    def test_set2(self):
        # encrypted text in plain english
        # print(self.buf_x_bytes)
        # => b'\x1c\x01\x11\x00\x1f\x01\x01\x00\x06\x1a\x02KSSP\t\x18\x1c'

        # encryption key in plain english
        # print(self.buf_y_bytes)
        # => b"hit the bull's eye"

        # target string in plain english
        # print(binascii.unhexlify(self.target))
        # => b"the kid don't play" 

        xor_result = xor(self.buf_x_bytes, self.buf_y_bytes)

        # xor result in plain english
        # print(xor_result)
        # => b"the kid don't play"

        # target is plain ascii so convert result for testing..
        self.assertEqual(self.target, binascii.hexlify(xor_result).decode("ASCII"))

if __name__ == '__main__':
    unittest.main()
