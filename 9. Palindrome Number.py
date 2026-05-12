class Solution:
    def isPalindrome(self, x):
        
        # Số âm chắc chắn không phải palindrome
        if x < 0:
            return False
        
        # Số kết thúc bằng 0 (trừ 0) cũng không phải palindrome
        if x != 0 and x % 10 == 0:
            return False
        
        reversed_half = 0
        
        # Đảo một nửa số
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # So sánh:
        # - Với số chẵn chữ số: x == reversed_half
        # - Với số lẻ chữ số: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10