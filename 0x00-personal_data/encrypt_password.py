#!/usr/bin/env python3
"""
Defines a function for salting and hashing a password.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if password mathes the hash."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
