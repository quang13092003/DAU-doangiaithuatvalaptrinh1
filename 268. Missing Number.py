class Solution:
    def missingNumber(self, nums):
        
        n = len(nums)
        
        # Tổng các số từ 0 -> n
        total = n * (n + 1) // 2
        
        # Trừ đi tổng các phần tử trong mảng
        # Số còn lại chính là số bị thiếu
        return total - sum(nums)