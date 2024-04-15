#!/usr/bin/env python3
"""
Defines a class for handling authentication.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Class for handling authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """TODO: update docstring"""
        return False

    def authorization_header(self, request=None) -> str:
        """TODO: implement"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """TODO: implement"""
        return None
