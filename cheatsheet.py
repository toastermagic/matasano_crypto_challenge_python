#!/usr/bin/env python

print("# a byte string displayed as ascii (input: b'test')")
b = b"test"
print(b) # => b"test"
print()

print("# convert ascii bytes to hex representation (input: b'test')")
b = b"test".hex() # => 74657374 
print(b)
print()

print("# convert ascii hex representation of bytes to a byte string (input: '74657374')")
b = bytes.fromhex(b) # => b"test" 
print(b)
print()

print("# print bytes with string interpolation")
print("bytes interpolation: " + str(b)) # => bytes interpolation: b'\xde\xad\xbe\xef'
print()

# NOTE: prefer binascii functions since they always returns bytes

import binascii

print("# convert bytes to hex (input: b'test')")
print(binascii.hexlify(b"test")) # => b"74657374"
print()

print("# convert ascii hex to bytes (input: '74657374')")
print(binascii.unhexlify("74657374")) # => b"test"
print()

print("# convert bytes to ascii (input: b'test')")
print(b'test'.decode("ASCII")) # => "test"
print()

print("# convert ascii to bytes (input: 'test')")
print('test'.encode("ASCII")) # => b"test"
print()

