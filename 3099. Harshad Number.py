class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x):
        
        # Tính tổng các chữ số
        digit_sum = sum(int(d) for d in str(x))
        
        # Nếu x chia hết cho tổng chữ số -> là Harshad
        if x % digit_sum == 0:
            return digit_sum
        
        return -1