#!/usr/bin/env python

import sys

def xor(buf_x_bytes, buf_y_bytes):
    """binary xor two sets of bytes"""
    return bytes(x ^ y for x, y in zip(buf_x_bytes, buf_y_bytes))

def repeating_xor(message, key):
    """binary xor two sets of bytes where the second set of bytes is a repeated key"""

    message_length = len(message)+1

    repeated_key = (key * message_length)[:message_length]

    return bytes(x ^ y for x, y in zip(message, repeated_key))
