import string

def is_pangram(s):
    result = set(string.ascii_lowercase)
    return set(s.lower()) >= result