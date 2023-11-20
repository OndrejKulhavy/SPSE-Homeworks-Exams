import re

"""
This method checks if the password is valid or not. Based on this parameters:
    - The password must be at least 10 characters long.
    - The password must contain at least one number.
    - The password must contain at least one lowercase and one uppercase letter.
    - The password must contain at least one non-alphanumeric character.
    - The password must not contain the username.
    - The password must not contain any substring of the username longer than 3 characters.
"""


def password_policy_regex_check(username: str, password: str):
    # is longer than 10