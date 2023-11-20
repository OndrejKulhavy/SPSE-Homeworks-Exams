import re


def is_email_valid(email_address):
    EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.search(EMAIL_REGEX, email_address):
        return True
    return False


def change_user_email(username, new_email):
    if not is_email_valid(new_email):
        raise ValueError("Email address is not valid")
    sql = f"UPDATE users SET email = '{new_email}' WHERE username = {username}"
    return sql


assert is_email_valid("okulhav@gmail.com") == True
assert is_email_valid("okulhav@gmailcom") == False
assert is_email_valid("okulhav@@@@gmail.com") == False
assert change_user_email("okulhav",
                         "okulhav@gmail.com") == "UPDATE users SET email = 'okulhav@gmail.com' WHERE username = okulhav"
