class Solution:
    def isPowerOfFour(self, n):
        
        # Số <= 0 không hợp lệ
        if n <= 0:
            return False
        
        # Điều kiện:
        # 1. Là power of 2: n & (n - 1) == 0
        # 2. Bit 1 nằm ở vị trí chẵn (mask 0x55555555)
        
        return (n & (n - 1)) == 0 and (n & 0x55555555) != 0