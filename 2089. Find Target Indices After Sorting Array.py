class Solution:
    def targetIndices(self, nums, target):
        count_less = 0
        count_equal = 0
        
        for num in nums:
            if num < target:
                count_less += 1
            elif num == target:
                count_equal += 1
        
        return [count_less + i for i in range(count_equal)]