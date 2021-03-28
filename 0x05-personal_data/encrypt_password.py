#!/usr/bin/env python3
""" 
hash_password
is_valid
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password, which is a byte string"""
    encoded = str.encode(password)
    hashed_password = bcrypt.hashpw(encoded, bcrypt.gensalt())
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates that the provided password matches the hashed password"""
    encoded = str.encode(password)
    if bcrypt.checkpw(encoded, hashed_password):
        return True
    else:
        return False
