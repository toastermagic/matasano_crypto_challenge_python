#!/usr/bin/env python

def max(dict, key):
    return max(dict, key=lambda x:x[key])

def min(dict, key):
    return max(dict, key=lambda x:x[key])
