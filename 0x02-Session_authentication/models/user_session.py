#!/usr/bin/env python3
"""
UserSession model
"""
from models.base import Base
import json
import os


class UserSession(Base):
    """UserSession class"""

    __file_path = "user_sessions.json"
    __objects = []

    def __init__(self, *args: list, **kwargs: dict):
        """Initialize a UserSession instance"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')

    def save(self):
        """Save the current instance to the list of objects"""
        self.__class__.__objects.append(self)

    @classmethod
    def save_to_file(cls):
        """Save all objects to a file"""
        with open(cls.__file_path, 'w') as f:
            json.dump([obj.to_dict() for obj in cls.__objects], f)

    @classmethod
    def load_from_file(cls):
        """Load all objects from a file"""
        if os.path.exists(cls.__file_path):
            with open(cls.__file_path, 'r') as f:
                cls.__objects = [cls(**obj) for obj in json.load(f)]

    @classmethod
    def search(cls, filters):
        """Search for objects that match the given filters"""
        results = []
        for obj in cls.__objects:
            match = True
            for key, value in filters.items():
                if getattr(obj, key) != value:
                    match = False
                    break
            if match:
                results.append(obj)
        return results

    def remove(self):
        """Remove the current instance from the list of objects"""
        self.__class__.__objects = [obj for obj in self.__class__.__objects if obj != self]
