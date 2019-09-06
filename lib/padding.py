#!/usr/bin/env python

def pad(bytes, blocksize):
    if len(bytes) <= blocksize:
        # no padding necessary
        if (len(bytes) % blocksize == 0):
            return bytes

        padding_byte = blocksize - len(bytes)

        if padding_byte == 0:
            padding_byte = blocksize
