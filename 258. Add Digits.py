class Solution:
    def addDigits(self, num):
        
        # Dùng công thức digital root:
        # Nếu num = 0 -> trả 0
        if num == 0:
            return 0
        
        # Kết quả = 1 + (num - 1) % 9
        return 1 + (num - 1) % 9