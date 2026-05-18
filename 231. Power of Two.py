class Solution:
    def isPowerOfTwo(self, n):
        
        # Số <= 0 chắc chắn không phải
        if n <= 0:
            return False
        
        # Nếu là lũy thừa của 2:
        # chỉ có đúng 1 bit = 1 trong biểu diễn nhị phân
        # n & (n - 1) sẽ = 0
        return (n & (n - 1)) == 0