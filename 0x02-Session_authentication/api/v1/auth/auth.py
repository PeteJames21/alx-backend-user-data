#!/usr/bin/env python3
"""
Defines a class for handling authentication.
"""

from typing import List, TypeVar
import os
import re


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
            # Attempt to match any paths ending with '*' in excluded_paths
            wildcards = filter(lambda s: s.endswith('*'), excluded_paths)
            for regex in wildcards:
                if re.match(regex, path):
                    return False
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

    def session_cookie(self, request=None):
        """Get the value of the cookie defined by the SESSION_NAME env var."""
        if not request:
            return None
        session_name = os.environ.get('SESSION_NAME')
        return request.cookies.get(session_name)
