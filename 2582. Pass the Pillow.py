class Solution:
    def passThePillow(self, n, time):
        
        # Một chu kỳ đi + về có độ dài:
        cycle = 2 * (n - 1)
        
        # Thời gian trong 1 chu kỳ
        t = time % cycle
        
        # Nếu đang đi xuôi
        if t < n:
            return 1 + t
        
        # Nếu đang đi ngược
        return n - (t - (n - 1))