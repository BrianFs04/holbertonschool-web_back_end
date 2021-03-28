#!/usr/bin/env python3
""" hash_password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    encoded = str.encode(password)
    hashed_password = bcrypt.hashpw(encoded, bcrypt.gensalt())
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    encoded = str.encode(password)
    if bcrypt.checkpw(encoded, hashed_password):
        return True
    else:
        return False
