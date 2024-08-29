# ALX 0x00-personal_data

## Overview

Welcome to the ALX Backend User Data project! This project focuses on handling personal data securely, including logging, database connections, and password encryption. By the end of this project, you will have a solid understanding of how to manage and protect sensitive information in a backend system.

## Project Timeline

- **Start Date**: August 28, 2024, 6:00 AM
- **End Date**: August 30, 2024, 6:00 AM
- **Checker Release**: August 28, 2024, 6:00 PM
- **Manual QA Review**: August 30, 2024, 12:26 AM
- **Auto Review**: At the project deadline

## Resources

To complete this project, you will need to read or watch the following resources:

- [What Is PII, non-PII, and Personal Data?](#)
- [Logging Documentation](#)
- [bcrypt Package](#)
- [Logging to Files, Setting Levels, and Formatting](#)

## Learning Objectives

By the end of this project, you should be able to:

- Identify examples of Personally Identifiable Information (PII).
- Implement a log filter to obfuscate PII fields.
- Encrypt passwords and validate input passwords.
- Authenticate to a database using environment variables.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Your code should use the `pycodestyle` style (version 2.5).
- All files must be executable.
- The length of your files will be tested using `wc`.
- All modules should have documentation.
- All classes should have documentation.
- All functions (inside and outside a class) should have documentation.
- All functions should be type annotated.

## Tasks

### Task 0: Regex-ing

Write a function called `filter_datum` that returns the log message obfuscated.

### Task 1: Log Formatter

Copy the provided code into `filtered_logger.py` and update the `RedactingFormatter` class to accept a list of fields and filter values in incoming log records.

### Task 2: Create Logger

Implement a `get_logger` function that returns a `logging.Logger` object configured to use `RedactingFormatter`.

### Task 3: Connect to Secure Database

Implement a `get_db` function that returns a connector to the database using credentials stored in environment variables.

### Task 4: Read and Filter Data

Implement a `main` function that retrieves all rows in the `users` table and logs each row under a filtered format.

### Task 5: Encrypting Passwords

Implement a `hash_password` function that returns a salted, hashed password using the `bcrypt` package.

### Task 6: Check Valid Password

Implement an `is_valid` function that validates if the provided password matches the hashed password using `bcrypt`.

## Usage

### Setting Up Environment Variables

```bash
export PERSONAL_DATA_DB_USERNAME=root
export PERSONAL_DATA_DB_PASSWORD=root
export PERSONAL_DATA_DB_HOST=localhost
export PERSONAL_DATA_DB_NAME=my_db
