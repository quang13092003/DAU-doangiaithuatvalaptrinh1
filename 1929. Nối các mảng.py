class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = []

        for i in range(n):
            ans.append(nums[i])
        for i in range(n):
            ans.append(nums[i])

        return ans
