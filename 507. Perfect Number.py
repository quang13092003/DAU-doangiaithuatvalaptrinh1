class Solution:
    def checkPerfectNumber(self, num):
        
        # 1 không phải perfect number
        if num == 1:
            return False
        
        total = 1  # 1 luôn là ước
        
        # Duyệt từ 2 -> sqrt(num)
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                
                # Nếu i không phải căn bậc 2
                if i != num // i:
                    total += num // i
            i += 1
        
        # So sánh tổng ước (trừ chính nó)
        return total == num