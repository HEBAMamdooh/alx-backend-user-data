#!/usr/bin/env python3
"""
Main file
"""
import requests
from user import User

BASE_URL = "http://127.0.0.1:5000"


def register_user(email: str, password: str):
    response = requests.post(f"{BASE_URL}/users",
                             data={"email": email, "password": password})
    assert response.status_code == 200, f"Failed to register user: {
        response.text}"


def main():
    email = "test@example.com"
    password = "secure_password"
    register_user(email, password)


if __name__ == "__main__":
    main()
