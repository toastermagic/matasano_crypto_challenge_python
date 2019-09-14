#!/usr/bin/env python3
#
# 4. Byte-at-a-time ECB decryption, Full control version
#
# Copy your oracle function to a new function that encrypts buffers
# under ECB mode using a consistent but unknown key (for instance,
# assign a single random key, once, to a global variable).
#
# Now take that same function and have it append to the plaintext,
# BEFORE ENCRYPTING, the following string:
#
#   Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
#   aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
#   dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
#   YnkK
#
# SPOILER ALERT: DO NOT DECODE THIS STRING NOW. DON'T DO IT.
#
# Base64 decode the string before appending it. DO NOT BASE64 DECODE THE
# STRING BY HAND; MAKE YOUR CODE DO IT. The point is that you don't know
# its contents.
#
# What you have now is a function that produces:
#
#   AES-128-ECB(your-string || unknown-string, random-key)
#
# You can decrypt "unknown-string" with repeated calls to the oracle
# function!
#
# Here's roughly how:
#
# a. Feed identical bytes of your-string to the function 1 at a time ---
# start with 1 byte ("A"), then "AA", then "AAA" and so on. Discover the
# block size of the cipher. You know it, but do this step anyway.
#
# b. Detect that the function is using ECB. You already know, but do
# this step anyways.
#
# c. Knowing the block size, craft an input block that is exactly 1 byte
# short (for instance, if the block size is 8 bytes, make
# "AAAAAAA"). Think about what the oracle function is going to put in
# that last byte position.
#
# d. Make a dictionary of every possible last byte by feeding different
# strings to the oracle; for instance, "AAAAAAAA", "AAAAAAAB",
# "AAAAAAAC", remembering the first block of each invocation.
#
# e. Match the output of the one-byte-short input to one of the entries
# in your dictionary. You've now discovered the first byte of
# unknown-string.
#
# f. Repeat for the next byte.


# example decryption for: SECRET FOREST ORANGE
#
# first iteration:
#
# encrypt(<known text> | secret | padding) <- block -1
# iterate through every byte until byte is found
# change "known text"
# 
#
# AAAAAS ECRETF ORESTO RANGEP <= first target_cipher
#
# AAAASE CRETFO RESTOR ANGEPP
# AAASEC RETFOR ESTORA NGEPPP
# AASECR ETFORE STORAN GEPPPP
# ASECRE TFORES TORANG EPPPPP
# SECRET FOREST ORANGE PPPPPP
#
# XXXXXX
#    ^- target block
#
# second iteration:
#
# SECRET AAAAAT ORANGE PPPPPP <= first target_cipher
#
# SECRET AAAAST ORANGE PPPPPP
# SECRET AAAEST ORANGE PPPPPP
# SECRET AAREST ORANGE PPPPPP
# SECRET AOREST ORANGE PPPPPP
# SECRET FOREST ORANGE PPPPPP
#
#        XXXXXX
#           ^- target block
#
# third iteration:
#
# SECRET FOREST AAAAAE PPPPPP <= first target_cipher
#
# SECRET FOREST AAAAGE PPPPPP
# SECRET FOREST AAANGE PPPPPP
# SECRET FOREST AAANGE PPPPPP
# SECRET FOREST ARANGE PPPPPP
# SECRET FOREST ORANGE PPPPPP
#
#               XXXXXX
#                  ^- target block



import sys
sys.path.append('../lib')

import unittest
import time
from base64 import *
from pprint import pprint
from random import randint
import re
from padding import *
from ecb import *
from key import *


class TestChallenge4(unittest.TestCase):
    SECRET = b64decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg" \
           + "aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq" \
           + "dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg" \
           + "YnkK")

    # consistent but *unknown* key
    with open("../set2/data/12-key.txt", encoding="ISO-8859-1") as file:
        KEY = b64decode(file.read())

    def test_challenge4(self):
        block_size = 16

        broken_bytes = ""

        block_count = int(len(b"a" * block_size + pad(SECRET, len(KEY))) / block_size)

        for block in range(0, block_count):
            # 15..0
            for position in range(block_size - 1, -1, -1):
                known_text = b"A" * position

                reference_cipher_text = encryption_oracle(known_text)

                broken_bytes += break_ecb(position, known_text, reference_cipher_text, broken_bytes, block, block_size)

        print(broken_bytes)

def break_ecb(position, known_text: bytes, reference_cipher_text, broken_bytes, block, block_size):
    for char in range(0, 127):
        prefix = known_text + broken_bytes.encode("ASCII") + chr(char).encode("ASCII")

        encrypted_data = encryption_oracle(prefix)

        offset = block_size + (block * block_size)

        if encrypted_data[0:offset] == reference_cipher_text[0:offset]:
            return chr(char)

    return ""


def encryption_oracle(plain_text: bytes) -> bytes:
    cipher = AES.new(KEY, AES.MODE_ECB)
    padded_plain_text = pad(plain_text + SECRET, len(KEY))
    return cipher.encrypt(padded_plain_text)

if __name__ == '__main__':
    unittest.main()
