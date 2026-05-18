class Solution:
    def canAliceWin(self, n):
        
        # Alice đi trước, lấy 10 viên
        take = 10
        alice_turn = True
        
        while n >= take:
            n -= take
            
            # đổi lượt
            alice_turn = not alice_turn
            take -= 1
        
        # Nếu tới lượt Alice mà không đủ đá -> Alice thua
        return not alice_turn