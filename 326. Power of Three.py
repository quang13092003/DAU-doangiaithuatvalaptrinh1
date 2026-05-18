class Solution:
    def isPowerOfThree(self, n):
        
        # Số <= 0 chắc chắn không phải
        if n <= 0:
            return False
        
        # Chia liên tục cho 3
        while n % 3 == 0:
            n //= 3
        
        # Nếu còn lại 1 -> là lũy thừa của 3
        return n == 1