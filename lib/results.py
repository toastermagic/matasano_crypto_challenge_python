#!/usr/bin/env python3

def find_max(data, key):
    return max(data, key=lambda x:x[key])

def find_min(data, key):
    return min(data, key=lambda x:x[key])

def sort(data, key):
    return sorted(data, key=lambda x:x[key])
