#!/usr/bin/env python

import unittest
from single_byte_xor import *
from pprint import pprint

class TestSet4(unittest.TestCase):
    data = open("data/4.txt", encoding="ISO-8859-1")
    target = "Now that the party is jumping\n"

    def test_set4(self):
        results = []
        line_no = 0

        # generate all permutations of each line xor'd with each ascii char
        for line in self.data:
            line_no += 1
            line = line.strip()
            result = max_score_message(score(line))
            result["line_no"] = line_no
            results.append(result)

        message_with_top_score = max(results, key=lambda x:x['score'])

        #pprint(message_with_top_score)
        # => {'key': '5',
        #     'line_no': 171,
        #     'message': 'Now that the party is jumping\n',
        #     'score': 261.13899999999995}

        self.assertEqual(self.target, message_with_top_score["message"])

if __name__ == '__main__':
    unittest.main()
