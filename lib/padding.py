#!/usr/bin/env python3

# PKCS #7 RFC: https://tools.ietf.org/html/rfc2315#section-10.3
def pad(message, block_length):
    message_length = len(message)

    if block_length > 255:
        raise Exception("maximum block size is 255!")

    # pad messages that are divisible by block length so decryption
    # has some bytes to detect
    if message_length == block_length or message_length % block_length == 0:
        padding_byte = block_length

    # FIXME
    # message is larger than block length, so workout remainder to use as padding
    if message_length > block_length:
        padding_byte = block_length - (message_length % block_length)

    # message is shorter than block length so calculate extra padding to equalize
    if message_length < block_length:
        padding_byte = block_length - message_length

    padding = bytes([padding_byte]) * padding_byte

    return message + padding