class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        count = [0] * 50
        
        for i in range(lowLimit, highLimit + 1):
            s = sum(map(int, str(i)))
            count[s] += 1
        
        return max(count)