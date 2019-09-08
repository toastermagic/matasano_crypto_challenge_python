#!/usr/bin/env python3

from Crypto.Cipher import AES
from padding import *
from iteration_utilities import grouper
from xor import xor

def decrypt_ecb_cbc(cipher_text, key, iv):
    block_length = len(key)

    if len(iv) != block_length:
        raise Exception("iv must match key length!")

    blocks       = list(grouper(cipher_text, block_length))
    cipher       = AES.new(key, AES.MODE_ECB)
    last_block   = iv
    plain_blocks = []

    # the blocks seem to be backwards!
    for block in blocks:
        decrypted_block = cipher.decrypt(bytes(block))
        plain_block = xor(decrypted_block, last_block)
        plain_blocks.append(plain_block)
        print(last_block)
        last_block = plain_block

    # TODO: remove padding - should be 11 bytes of \x0B

    return b"".join(plain_blocks)

def encrypt_ecb_cbc(message, key, iv):
    block_length = len(key)

    if len(iv) != block_length:
        raise Exception("iv must match key length!")

    padded_message = pad(message, block_length)

    blocks           = list(grouper(padded_message, block_length))
    cipher           = AES.new(key, AES.MODE_ECB)
    last_block       = iv
    encrypted_blocks = []

    for block in blocks:
        encrypted_block = cipher.encrypt(xor(last_block, block))
        encrypted_blocks.append(encrypted_block)
        last_block = encrypted_block

    return b"".join(encrypted_blocks)
