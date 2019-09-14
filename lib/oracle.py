#!/usr/bin/env python

from Crypto.Cipher import AES
from padding import *

def encryption_oracle(oracle_context, plain_text: bytes) -> bytes:
    cipher = AES.new(oracle_context["key"], AES.MODE_ECB)
    block_size = len(oracle_context["key"])
    padded_plain_text = pad(plain_text + oracle_context["secret"], block_size)
    return cipher.encrypt(padded_plain_text)
