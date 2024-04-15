#!/usr/bin/env python3
"""
Defines a class for handling authentication.
"""

from typing import List, TypeVar


class Auth:
    """Class for handling authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if a path requires authentication."""
        if not path or not excluded_paths:
            return True

        # Strip trailing slashes
        excluded_paths = [s.rstrip('/') for s in excluded_paths]
        path = path.rstrip('/')

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """Return the authorization header, or None if not found."""
        if not request:
            return None
        auth_header = request.headers.get('Authorization', None)
        return auth_header

    def current_user(self, request=None) -> TypeVar('User'):
        """TODO: implement"""
        return None
