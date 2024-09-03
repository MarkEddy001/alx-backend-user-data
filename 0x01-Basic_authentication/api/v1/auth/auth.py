#!/usr/bin/env python3
""" API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ manages the API authentication """
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if a given path requires authentication

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not require authentication.

        Returns:
            bool: True if the path requires authentication, False otherwise.
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True

        # Normalize the path
        if path[-1] != '/':
            path += '/'

        for p in excluded_paths:
            # Normalize the excluded path
            if p[-1] != '/':
                p += '/'
            if p.endswith('*'):
                if path.startswith(p[:-1]):
                    return False
            elif path == p:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Returns the value of the Authorization header from a request object

        Args:
            request (object, optional): The request object (default: None).

        Returns:
            str: The value of the Authorization header, or None if not present.
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Placeholder method to be implemented in child classes

        Args:
            request (object, optional): The request object (default: None).

        Returns:
            TypeVar('User'): The current user, or None if not implemented.
        """
        return None
