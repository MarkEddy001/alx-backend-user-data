#!/usr/bin/env python3
"""manage the API authentication"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from models.user import User
import base64


class BasicAuth(Auth):
    """BasicAuth Class"""
    
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""
        if authorization_header is None or not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string"""
        if base64_authorization_header is None or not isinstance(base64_authorization_header, str):
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            return message_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None or not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
            if not users:
                return None
            user = users[0]
            if user.is_valid_password(user_pwd):
                return user
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request"""
        try:
            header = self.authorization_header(request)
            if header is None:
                return None
            base64_h = self.extract_base64_authorization_header(header)
            if base64_h is None:
                return None
            decode_h = self.decode_base64_authorization_header(base64_h)
            if decode_h is None:
                return None
            email, password = self.extract_user_credentials(decode_h)
            if email is None or password is None:
                return None
            return self.user_object_from_credentials(email, password)
        except Exception:
            return None
