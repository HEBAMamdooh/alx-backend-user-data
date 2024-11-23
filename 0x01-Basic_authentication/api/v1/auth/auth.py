#!/usr/bin/env python3
"""
Auth module for API authentication.
"""
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """Template for all authentication mechanisms."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determine if a path requires authentication."""
        if path is None or not excluded_paths:
            return True
        for p in excluded_paths:
            if p.endswith('*') and path.startswith(p[:-1]):
                return False
            if p == path or (p[-1] == '/' and path.startswith(p[:-1])):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Retrieve the Authorization header from the request."""
        if not request:
            return None

    def current_user(self, request=None) -> User:
        """Retrieve the current user."""
        return None

    def current_user(self, request=None) -> User:
        """Retrieve the current user."""
        return None
