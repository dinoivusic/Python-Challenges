class Solution:
    def rotate(self, nums,k):
        for _ in range(k):
            nums.insert(0, nums[-1])
            nums.pop()
        return nums
