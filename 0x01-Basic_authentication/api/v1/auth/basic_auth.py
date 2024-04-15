#!/usr/bin/env python3
"""
Defines a class for performing basic authentication.
"""

from .auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode a base64 encoded string."""
        if not base64_authorization_header:
            return None
        try:
            s = base64.b64decode(base64_authorization_header)
            return s.decode('utf-8')
        except Exception:
            return None
