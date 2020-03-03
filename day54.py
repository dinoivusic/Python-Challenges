def strStr(self, haystack: str, needle: str) -> int:
    x = haystack.find(needle)
    if needle in haystack:
        return haystack.index(needle)
    return -1