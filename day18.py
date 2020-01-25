class Solution:
    def isPalindrome(self, strs):
        s = [c.lower() for c in strs if c.isalnum()]
        if s == s[::-1]:
            return True
        return False
