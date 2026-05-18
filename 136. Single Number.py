class Solution:
    def singleNumber(self, nums):
        
        # Dùng phép XOR:
        # a ^ a = 0
        # a ^ 0 = a
        # => các số trùng nhau sẽ triệt tiêu
        
        result = 0
        
        for num in nums:
            result ^= num
        
        return result