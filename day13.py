class Solution:
    def plus_one(self, digits):
        string = " "
        for i in digits:
            string += str(i)
        ans = int(string)+1
        res = []
        for j in str(ans):
            res.append(int(j))
        return res
