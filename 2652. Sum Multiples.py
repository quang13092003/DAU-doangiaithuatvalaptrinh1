class Solution:
    def sumOfMultiples(self, n):
        
        total = 0
        
        # Duyệt từ 1 -> n
        for i in range(1, n + 1):
            
            # Nếu chia hết cho 3 hoặc 5 hoặc 7
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total += i
        
        return total