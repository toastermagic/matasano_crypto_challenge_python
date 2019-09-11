#!/usr/bin/env python

from random import randint

def random_key(length):
    key = b""
    for i in range(0, length):
        key += bytes([randint(1,254)])

    return key

