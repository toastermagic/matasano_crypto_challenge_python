#!/usr/bin/env python

# PKCS #7 RFC: https://tools.ietf.org/html/rfc2315#section-10.3
def pad(message, block_length):
    message_length = len(message)

    if block_length > 255:
        raise Exception("maximum block size is 255!")

    # padding unnecessary since block length matches number of bytes
    if message_length == block_length:
        return message

    # padding unnecessary since message is divisible by block length
    if message_length % block_length == 0:
        return message

    # message is larger than block length, so workout remainder to use as padding
    if message_length > block_length:
        padding_byte = block_length - (message_length % block_length)

    # message is shorter than block length so calculate extra padding to equalize
    if message_length < block_length:
        padding_byte = block_length - message_length

    padding = bytes([padding_byte]) * padding_byte

    return message + padding

