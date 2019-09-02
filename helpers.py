#!/usr/bin/env python

import sys

def xor(buf_x_bytes, buf_y_bytes):
    """binary xor two sets of bytes"""
    return bytes(x ^ y for x, y in zip(buf_x_bytes, buf_y_bytes))

def repeating_xor(message, key):
    """binary xor two sets of bytes where the second set of bytes is a repeated key"""

    message_length = len(message)

    repeated_key = (key * message_length)[:message_length]
    print(message)
    print(repeated_key)

    return bytes(x ^ y for x, y in zip(message.encode("ASCII"), repeated_key.encode("ASCII")))
