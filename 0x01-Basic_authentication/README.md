# Basic Authentication API

## Overview
This project demonstrates the implementation of Basic Authentication on a simple API using Python and Flask. The goal is to understand the authentication process by building it from scratch.

## Background Context
In the industry, it's recommended to use established modules or frameworks for authentication (e.g., Flask-HTTPAuth in Python-Flask). However, for learning purposes, this project walks through each step of the Basic Authentication mechanism to understand it by doing.

## Learning Objectives
By the end of this project, you should be able to explain the following concepts:
- What authentication means
- What Base64 is
- How to encode a string in Base64
- What Basic Authentication means
- How to send the Authorization header

## Resources
To get started, you should read or watch the following resources:
- [REST API Authentication Mechanisms](https://example.com)
- [Base64 in Python](https://example.com)
- [HTTP header Authorization](https://example.com)
- [Flask](https://example.com)
- [Base64 - concept](https://example.com)

## Requirements
- **Python Scripts**:
  - All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
  - All files should end with a new line.
  - The first line of all files should be exactly `#!/usr/bin/env python3`.
  - A `README.md` file at the root of the project folder is mandatory.
  - Code should follow the `pycodestyle` style (version 2.5).
  - All files must be executable.
  - The length of files will be tested using `wc`.
  - All modules should have documentation.
  - All classes should have documentation.
  - All functions (inside and outside a class) should have documentation.
  - Documentation should be a real sentence explaining the purpose of the module, class, or method.

## Setup and Usage
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/alx-backend-user-data.git
    cd alx-backend-user-data/0x01-Basic_authentication
    ```

2. **Install dependencies**:
    ```sh
    pip3 install -r requirements.txt
    ```

3. **Start the server**:
    ```sh
    API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
    ```

4. **Test the API**:
    - In another terminal or browser, use the following command to check the API status:
      ```sh
      curl "http://0.0.0.0:5000/api/v1/status"
      ```

## Project Tasks
### 0. Simple-basic-API
- Set up a simple API with a User model and start the server.

### 1. Error handler: Unauthorized
- Implement an error handler for unauthorized requests (HTTP status code 401).

### 2. Error handler: Forbidden
- Implement an error handler for forbidden requests (HTTP status code 403).

### 3. Auth class
- Create a class to manage API authentication.

### 4. Define which routes don't need authentication
- Update the `require_auth` method to handle excluded paths.

### 5. Request validation!
- Validate all requests to secure the API.

### 6. Basic auth
- Create a class `BasicAuth` that inherits from `Auth`.

### 7. Basic - Base64 part
- Extract the Base64 part of the Authorization header for Basic Authentication.

### 8. Basic - Base64 decode
- Decode the Base64 part of the Authorization header.

### 9. Basic - User credentials
- Extract user email and password from the Base64 decoded value.

### 10. Basic - User object
- Retrieve the User instance based on email and password.

### 11. Basic - Overload current_user - and BOOM!
- Complete the Basic authentication by retrieving the User instance for a request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to the ALX program for providing the project framework and resources.
