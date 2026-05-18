class Solution:
    def minimumMoves(self, s):
        
        moves = 0
        i = 0
        n = len(s)
        
        # Duyệt chuỗi
        while i < n:
            
            # Nếu gặp 'X' -> thực hiện 1 lần chuyển đổi
            if s[i] == 'X':
                moves += 1
                
                # Bỏ qua 3 ký tự vì đã chuyển thành 'O'
                i += 3
            else:
                # Nếu là 'O' -> đi tiếp
                i += 1
        
        return moves