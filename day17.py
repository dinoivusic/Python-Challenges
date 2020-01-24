class Solution:
    def longestCommonPrefix(self, strs):
        longest = ""
        if len(strs) < 1:
            return longest
        for index, value in enumerate(strs[0]):
            longest += value
            for s in strs[1:]:
                if not s.startswith(longest):
                    return longest[:index]
        return longest
