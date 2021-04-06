#!/usr/bin/env python3
"""
BasicAuth module
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns the Base64 part of the Authorization
         header for a Basic Authentication"""
        if authorization_header is None or \
                not isinstance(authorization_header, str):
            return None

        splitted = authorization_header.split(" ")
        if splitted[0] != "Basic":
            return None
        else:
            return splitted[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Returns the decoded value of a Base64
        string base64_authorization_header"""
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
            return None

        try:
            return b64decode(base64_authorization_header).decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """Returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ":" not in decoded_base64_authorization_header:
            return None, None

        credentials = decoded_base64_authorization_header.split(":", 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Returns the User instance based on his email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({"email": user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Overloads Auth and retrieves the User instance for a request"""
        header = self.authorization_header(request)
        b64header = self.extract_base64_authorization_header(header)
        decodeb64 = self.decode_base64_authorization_header(b64header)
        credentials = self.extract_user_credentials(decodeb64)
        return self.user_object_from_credentials(credentials[0],
                                                 credentials[1])
