# Regex Password checker minimum eight characters, at least one uppercase letter,
# one lowercase letter and one number including special characters

import re
def password_checker():
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d$@$!%*?&]{8,}")
    try:
        password = input('Please enter your password')
    except ValueError:
        print('Please enter your password again')

    if pattern.match(password):
        print('It is a valid password')
    else:
        print('It is not a valid one')


if __name__ == "main":
    password_checker()
# Simple password checker, at least 8 chars long, with letters,numbers and @%$# and ends with a number


def simple_checker():
    pattern = re.compile(r"[A-Za-z0-9$@$!%*?&]{8,}\d")
    try:
        password = input('Please enter your password')
    except ValueError:
        print('Please enter your password again')

    if pattern.fullmatch(password):
        print('It is a valid password')
    else:
        print('It is not a valid one')


if __name__ == "main":
    simple_checker()
