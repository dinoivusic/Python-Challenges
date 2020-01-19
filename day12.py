class Solution:
    def intersect(self, nums1, nums2):

        tar, ite = [nums1, nums2] if len(nums2) >= len(nums1) else [nums2, nums1]

        if len(tar) == 0:
            return []

        arr = []
        i = 0

        while i < len(ite):
            el = ite[i]

            if el in tar and el in ite:
                arr.append(el)
                tar.remove(el)
            i += 1
        return arr
