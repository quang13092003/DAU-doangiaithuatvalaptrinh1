class Solution:
    def divisorGame(self, n):
        
        # Quy luật:
        # Nếu n là số chẵn -> Alice thắng
        # Nếu n là số lẻ -> Alice thua
        
        return n % 2 == 0