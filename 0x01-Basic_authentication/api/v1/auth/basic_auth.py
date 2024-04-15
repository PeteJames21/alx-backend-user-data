#!/usr/bin/env python3
"""
Defines a class for performing basic authentication.
"""

import base64
from .auth import Auth
from typing import TypeVar
from ..views.users import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Extract username and password from the auth header."""
        header = decoded_base64_authorization_header
        if not header or type(header) is not str:
            return None, None
        if ':' not in header:
            return None, None
        uname, pwd = header.split(':', maxsplit=1)
        return uname, pwd

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """Return the user matching the provided parameters."""
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None

        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception:
            return None
