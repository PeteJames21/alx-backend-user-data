#!/usr/bin/env python3
"""
Defines a class for handling session management.
"""
from .auth import Auth
from models.user import User
from uuid import uuid4
from typing import Union


class SessionAuth(Auth):
    """Class for handling session authentication."""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Generate a session id for the user_id."""
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) \
            -> Union[str, None]:
        """Get the user id associated with the given session id."""
        if not session_id or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """Return the user instance associated with the cookie value."""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """Delete the session associated with the given request."""
        if not request:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False
        del self.user_id_by_session_id[session_id]
        return True
