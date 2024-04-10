#!/usr/bin/env python3
"""
Defines a function for salting and hashing a password.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
