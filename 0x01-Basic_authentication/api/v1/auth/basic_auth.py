#!/usr/bin/env python3
"""
Defines a class for performing basic authentication.
"""

from .auth import Auth


class BasicAuth(Auth):
    """Class for handling basic authentication."""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Get the authorization type from the header."""
        if not authorization_header:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split('Basic ', maxsplit=1)[1]
