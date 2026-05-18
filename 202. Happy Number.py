class Solution:
    def isHappy(self, n):
        
        # Dùng set để phát hiện vòng lặp
        seen = set()
        
        while n != 1:
            # Nếu gặp lại số cũ -> bị loop -> không phải happy
            if n in seen:
                return False
            
            seen.add(n)
            
            # Tính tổng bình phương các chữ số
            n = sum(int(d)**2 for d in str(n))
        
        return True