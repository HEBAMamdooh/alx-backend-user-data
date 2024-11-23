#!/usr/bin/env python3
"""
BasicAuth module for API authentication.
"""
import base64
from typing import TypeVar, Optional, Tuple
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Basic Authentication class."""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extract the Base64 part of the Authorization header."""
        if not authorization_header or not isinstance(
            authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decode the Base64 string."""
        if not base64_authorization_header or not isinstance(
            base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header).decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """Extract user credentials from the decoded string."""
        if not decoded_base64_authorization_header or not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> Optional[User]:
        """Retrieve the User object by email and password."""
        if not user_email or not isinstance(user_email, str) or not user_pwd or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({"email": user_email})
            if not user:
                return None
            user = user[0]
            if not user.is_valid_password(user_pwd):
                return None
            return user
        except Exception:
            return None

    def current_user(self, request=None) -> Optional[User]:
        """Retrieve the current user."""
        header = self.authorization_header(request)
        if not header:
            return None
        base64_header = self.extract_base64_authorization_header(header)
        decoded_header = self.decode_base64_authorization_header(base64_header)
        email, password = self.extract_user_credentials(decoded_header)
        return self.user_object_from_credentials(email, password)
