class Solution:
    def decrypt(self, code, k):
        
        n = len(code)
        result = [0] * n
        
        # Nếu k = 0 -> tất cả = 0
        if k == 0:
            return result
        
        for i in range(n):
            total = 0
            
            # Nếu k > 0: cộng k phần tử phía sau
            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            
            # Nếu k < 0: cộng k phần tử phía trước
            else:
                for j in range(1, -k + 1):
                    total += code[(i - j) % n]
            
            result[i] = total
        
        return result