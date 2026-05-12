class Solution:
    def addBinary(self, a, b):
        
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []
        
        # Duyệt từ cuối về đầu
        while i >= 0 or j >= 0 or carry:
            
            total = carry
            
            # Nếu còn ký tự trong a
            if i >= 0:
                total += int(a[i])
                i -= 1
            
            # Nếu còn ký tự trong b
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # Thêm bit vào kết quả
            result.append(str(total % 2))
            
            # Cập nhật carry
            carry = total // 2
        
        # Đảo ngược kết quả vì đang thêm từ cuối
        return ''.join(result[::-1])