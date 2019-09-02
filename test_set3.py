#!/usr/bin/env python

import unittest
import single_byte_xor
from pprint import pprint

class TestSet3(unittest.TestCase):
    message = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    target = "Cooking MC's like a pound of bacon"

    def test_set2(self):
        result = single_byte_xor.max_score_result(single_byte_xor.generate_results(self.message))

        self.assertEqual(self.target, result["message"])

if __name__ == '__main__':
    unittest.main()
