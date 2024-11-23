#!/usr/bin/env python3
"""
Integration tests for the authentication service.
"""
import requests

BASE_URL = "http://127.0.0.1:5000"


def register_user(email: str, password: str):
    response = requests.post(f"{BASE_URL}/users", data={
        "email": email, "password": password})
    assert response.status_code == 200, response.text
    assert response.json()["message"] == "user created"


def main():
    email = "test@example.com"
    password = "password123"
    register_user(email, password)


if __name__ == "__main__":
    main()
