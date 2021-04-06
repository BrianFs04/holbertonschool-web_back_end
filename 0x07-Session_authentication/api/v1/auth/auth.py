#!/usr/bin/env python3
"""
Auth module
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path is excluded"""
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if "/" not in path[-1]:
            path += "/"
        for i in excluded_paths:
            if i.endswith("*") and path.startswith(i[:-1]):
                return False
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """Returns values form Authorization key"""
        if request is None or not request.headers.get("Authorization"):
            return None
        else:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None"""
        return None

    def session_cookie(self, request=None):
        """Returns a cookie value from a request"""
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)
