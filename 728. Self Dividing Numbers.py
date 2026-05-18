class Solution:
    def selfDividingNumbers(self, left, right):
        
        result = []
        
        # Duyệt từng số trong khoảng
        for num in range(left, right + 1):
            x = num
            valid = True
            
            # Kiểm tra từng chữ số
            while x > 0:
                digit = x % 10
                
                # Nếu có số 0 hoặc không chia hết
                if digit == 0 or num % digit != 0:
                    valid = False
                    break
                
                x //= 10
            
            if valid:
                result.append(num)
        
        return result