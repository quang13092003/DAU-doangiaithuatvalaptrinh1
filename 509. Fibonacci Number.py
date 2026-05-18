class Solution:
    def fib(self, n):
        
        # Trường hợp cơ bản
        if n <= 1:
            return n
        
        # Dùng 2 biến để lưu F(n-2) và F(n-1)
        a, b = 0, 1
        
        # Lặp từ 2 đến n
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        # b chính là F(n)
        return b