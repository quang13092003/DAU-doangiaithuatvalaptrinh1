class Solution:
    def isUgly(self, n):
        
        # Số <= 0 không phải ugly number
        if n <= 0:
            return False
        
        # Chia lần lượt cho 2, 3, 5
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        
        # Nếu còn lại 1 -> chỉ có các thừa số 2,3,5
        return n == 1