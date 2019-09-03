#!/usr/bin/env python

from base64 import b64decode
from pprint import pprint
from iteration_utilities import grouper
from xor import xor
from results import *

# hamming distance is number of differing bits between two xor'd strings
def hamming_distance(x, y):
    bytes = xor(x, y)

    collection = ""
    for byte in bytes: collection += "{0:08b}".format(byte)

    return collection.count("1")

def minimum_hamming_distances(bytes, keysize_range):
    results = []

    for keysize in keysize_range:
        hamming_distance_count = 0
        block_count = 0

        # iterate through sequential pairs of 'keysize' bytes, calculate
        # the hamming_distance(), add result to running total
        #
        # also pad lists in case bytes doesn't divide perfectly by keysize
        for values in grouper(list(grouper(bytes, keysize, fillvalue=0)), 2, fillvalue=[0]*keysize):
            block_count += 1
            buf_x = values[0]
            buf_y = values[1]

            hamming_distance_count += hamming_distance(buf_x, buf_y)/keysize

        results.append({
            "keysize":                     keysize,
            "normalized_hamming_distance": hamming_distance_count/block_count
        })

    return results
