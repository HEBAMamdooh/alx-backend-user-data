#!/usr/bin/env python3
"""
User model definition.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User object."""

    email: str = None
    password: str = None
    first_name: str = None
    last_name: str = None

    def is_valid_password(self, password: str) -> bool:
        """Validate the user's password."""
        return password == self.password
