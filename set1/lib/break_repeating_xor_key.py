#!/usr/bin/env python

from helpers import xor

# attempt key lengths from 2-40
for key_length in range(2, 41):
    print(f"key length: {key_length}")

# hamming distance is number of differing bits between two xor'd strings
def hamming_distance(x, y):
    bytes = xor(x, y)

    collection = ""
    for byte in bytes: collection += "{0:08b}".format(byte)

    return collection.count("1")

print(hamming_distance(b"this is a test", b"wokka wokka!!!"))
