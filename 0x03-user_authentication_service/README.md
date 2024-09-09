# User Authentication Service

This project implements a user authentication service using Flask and SQLAlchemy. The goal is to understand the mechanisms of user authentication by implementing them step-by-step.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
- [Tasks](#tasks)
  - [0. User model](#0-user-model)
  - [1. Create user](#1-create-user)
  - [2. Find user](#2-find-user)
  - [3. Update user](#3-update-user)
  - [4. Hash password](#4-hash-password)
  - [5. Register user](#5-register-user)
  - [6. Basic Flask app](#6-basic-flask-app)
  - [7. Register user endpoint](#7-register-user-endpoint)
  - [8. Credentials validation](#8-credentials-validation)
  - [9. Generate UUIDs](#9-generate-uuids)
  - [10. Get session ID](#10-get-session-id)
  - [11. Log in](#11-log-in)
  - [12. Find user by session ID](#12-find-user-by-session-id)
  - [13. Destroy session](#13-destroy-session)
  - [14. Log out](#14-log-out)
  - [15. User profile](#15-user-profile)
  - [16. Generate reset password token](#16-generate-reset-password-token)
  - [17. Get reset password token](#17-get-reset-password-token)
  - [18. Update password](#18-update-password)
  - [19. Update password endpoint](#19-update-password-endpoint)

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the `pycodestyle` style (version 2.5)
- Use SQLAlchemy 1.3.x
- All files must be executable
- The length of files will be tested using `wc`
- All modules should have documentation
- All classes should have documentation
- All functions (inside and outside a class) should have documentation
- All functions should be type annotated
- The Flask app should only interact with `Auth` and never with the database directly
- Only public methods of `Auth` and `DB` should be used outside these classes

## Setup

You will need to install `bcrypt`:

```sh
pip3 install bcrypt
