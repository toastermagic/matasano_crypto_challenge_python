#!/usr/bin/env python3

from Crypto.Cipher import AES
from padding import *
from iteration_utilities import grouper
from xor import xor
from results import *
from oracle import *

def decrypt_ecb_cbc(cipher_text, key, iv):
    block_length = len(key)

    if len(iv) != block_length:
        raise Exception("iv must match key length!")

    blocks       = list(grouper(cipher_text, block_length))
    cipher       = AES.new(key, AES.MODE_ECB)
    last_block   = iv
    plain_blocks = []

    for block in blocks:
        decrypted_block = cipher.decrypt(bytes(block))
        plain_block = xor(last_block, decrypted_block)
        plain_blocks.append(plain_block)
        last_block = block

    plain_text = pad_strip(b"".join(plain_blocks))
    return plain_text

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

def detect_ecb(collection, block_size):
    likely_ecb_texts = []
    index = 0

    # work out how many repeated chunks each entry has.
    # lots of repeated chunks means its likely ECB
    for data in collection:
        index += 1

        chunks = {}

        for chunk in list(grouper(data, block_size)):
            if tuple(chunk) in chunks.keys():
                chunks[tuple(chunk)] += 1
            else:
                chunks[tuple(chunk)] = 0

        repeated_chunk_total = sum(chunks.values())

        if repeated_chunk_total == 0:
            continue

        likely_ecb_texts.append({
            "block_size": block_size,
            "index": index,
            "cipher_text": data,
            "repeated_chunk_total": repeated_chunk_total
        })

    return likely_ecb_texts

def break_ecb(oracle_context, position, known_text: bytes, reference_cipher_text, broken_bytes, block, block_size):
    for char in range(0, 127):
        prefix = known_text + broken_bytes + chr(char).encode("ASCII")

        encrypted_data = encryption_oracle(oracle_context, prefix)

        offset = block_size + (block * block_size)

        if encrypted_data[0:offset] == reference_cipher_text[0:offset]:
            return chr(char).encode("ASCII")

    return b""

def break_ecb_byte_by_byte(oracle_context):
    block_size = 16

    broken_bytes = b""

    block_count = int(len(b"a" * block_size + pad(oracle_context["secret"], block_size)) / block_size)

    for block in range(0, block_count):
        # 15..0
        for position in range(block_size - 1, -1, -1):
            known_text = b"A" * position

            reference_cipher_text = encryption_oracle(oracle_context, known_text)

            broken_bytes += break_ecb(oracle_context, position, known_text,
                                      reference_cipher_text, broken_bytes, block, block_size)

    return broken_bytes
