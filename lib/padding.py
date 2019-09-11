#!/usr/bin/env python3

from random import randint

def pad_strip(message):
    padding_length = message[-1]
    return message[:- padding_length]

# PKCS #7 RFC: https://tools.ietf.org/html/rfc2315#section-10.3
def pad(message, block_length):
    message_length = len(message)

    if block_length > 255:
        raise Exception("maximum block size is 255!")

    # pad messages that are divisible by block length so decryption
    # has some bytes to detect
    if message_length == block_length or message_length % block_length == 0:
        padding_byte = block_length

    # message is longer than blocksize so message must be padded to multiple
    # of the block size
    if message_length > block_length:
        padding_byte = block_length - (message_length % block_length)

    # message is shorter than block length so calculate extra padding to equalize
    if message_length < block_length:
        padding_byte = block_length - message_length

    padding = bytes([padding_byte]) * padding_byte

    return message + padding

def pad_random(message, padding_length, placement):
    for i in range(0, padding_length):
        random_byte = bytes([randint(1, 254)])
        if placement == "prepend":
            message = random_byte + message

        if placement == "append":
            message = message + random_byte

    return message

