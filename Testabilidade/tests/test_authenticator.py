import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from authenticator import Authenticator

def test_authenticate_success():
    auth = Authenticator()
    assert auth.authenticate("user1", "password123") == "Access Granted"

def test_authenticate_failure():
    auth = Authenticator()
    assert auth.authenticate("user1", "wrongpassword") == "Access Denied"

def test_nonexistent_user():
    auth = Authenticator()
    assert auth.authenticate("unknown_user", "password123") == "Access Denied"
