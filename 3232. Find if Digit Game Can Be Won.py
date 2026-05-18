class Solution:
    def canAliceWin(self, nums):
        
        # Tổng số có 1 chữ số và 2 chữ số
        sum1 = 0
        sum2 = 0
        
        for num in nums:
            # Số 1 chữ số
            if num < 10:
                sum1 += num
            else:
                # Số 2 chữ số
                sum2 += num
        
        total = sum1 + sum2
        
        # Alice chọn 1 trong 2 nhóm:
        # - Nếu chọn 1 chữ số: thắng nếu sum1 > sum2
        # - Nếu chọn 2 chữ số: thắng nếu sum2 > sum1
        
        return sum1 > sum2 or sum2 > sum1