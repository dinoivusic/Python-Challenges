def isPalindrome(self, s: str) -> bool:
    string_list = [x.lower() for x in s if x.isalnum()]
    if string_list == string_list[::-1]:
        return True
    return False
