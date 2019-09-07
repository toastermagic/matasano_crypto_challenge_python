#!/usr/bin/env python3

import sys
sys.path.append('lib')

from results import *
from single_byte_xor import *

def detect_single_character_xor(data):
    results = []
    line_no = 0

    # generate permutations of each line xor'd with each ascii char
    for line in data:
        line_no += 1

        line = line.strip()

        result = find_max(score(line), "score")

        result["line_no"] = line_no

        results.append(result)

    return(results)

