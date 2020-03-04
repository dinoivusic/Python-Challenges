def longestCommonPrefix(self, strs: List[str]) -> str:
    ans = ""
    if len(strs) == 0:
        return ans
    for i in range(len(min(strs))):
        can = [s[i] for s in strs]
        if (len(set(can)) != 1):
            return ans
        ans += can[0]
    return ans

