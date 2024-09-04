# `Session_authentication`

![](https://miro.medium.com/v2/resize:fit:786/format:webp/1*-D6Ids2z9ebtz0_m9qeBBA.png)

## Background Context

In this project, you will implement a Session Authentication system. The goal is to understand the mechanism by implementing it step-by-step. Note that in a real-world scenario, you should use a module or framework that provides session authentication, such as Flask-HTTPAuth.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without the help of Google:

- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

## Requirements

### Python Scripts

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should use the `pycodestyle` style (version 2.5).
- All files must be executable.
- The length of files will be tested using `wc`.
- All modules should have documentation.
- All classes should have documentation.
- All functions (inside and outside a class) should have documentation.
- Documentation should be a real sentence explaining the purpose of the module, class, or method.

## Project Structure


## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/alx-backend-user-data.git
    cd alx-backend-user-data/0x02-Session_authentication
    ```

2. Ensure all files are executable:
    ```sh
    chmod +x api/v1/app.py
    ```

3. Run the application:
    ```sh
    API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
    ```

## Usage

### Endpoints

- **GET /api/v1/status**: Check the status of the API.
- **POST /api/v1/auth_session/login**: Log in with session authentication.
- **DELETE /api/v1/auth_session/logout**: Log out and destroy the session.
- **GET /api/v1/users/me**: Retrieve the authenticated User object.

### Example Requests

1. **Check API status**:
    ```sh
    curl "http://0.0.0.0:5000/api/v1/status"
    ```

2. **Log in**:
    ```sh
    curl -X POST "http://0.0.0.0:5000/api/v1/auth_session/login" -d "email=user@example.com" -d "password=your_password"
    ```

3. **Access user info with session cookie**:
    ```sh
    curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=<session_id>"
    ```

4. **Log out**:
    ```sh
    curl -X DELETE "http://0.0.0.0:5000/api/v1/auth_session/logout" --cookie "_my_session_id=<session_id>"
    ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- ALX for providing the project framework and guidelines.
- Flask documentation for reference.
