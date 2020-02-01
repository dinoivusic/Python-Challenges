class Solution:
    def numJewelsInStones(self, J, S):
        count = 0
        countdown = 0
        for char in S:
            if char in S and char in J:
                count += 1

        return count
