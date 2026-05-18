class Solution:
    def countElements(self, nums):
        mn = min(nums)
        mx = max(nums)
        
        count = 0
        for num in nums:
            if mn < num < mx:
                count += 1
        
        return count