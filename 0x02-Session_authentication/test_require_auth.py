#!/usr/bin/env python3
""" Test require_auth
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth("/api/v1/users", ["/api/v1/us*"]))  # False
print(a.require_auth("/api/v1/us", ["/api/v1/us*"]))  # False
print(a.require_auth("/api/v1/us/", ["/api/v1/us*"]))  # False
print(a.require_auth("/api/v1/uas", ["/api/v1/us*"]))  # True
print(a.require_auth("/api/v1/usual", ["/api/v1/us*"]))  # False
