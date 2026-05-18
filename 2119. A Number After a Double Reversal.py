class Solution:
    def isSameAfterReversals(self, num):
        
        # Số sau khi đảo 2 lần sẽ giữ nguyên
        # trừ khi số đó có số 0 ở cuối (bị mất khi đảo)
        
        # Trường hợp đặc biệt: 0 vẫn đúng
        if num == 0:
            return True
        
        # Nếu số chia hết cho 10 -> có số 0 cuối -> sai
        return num % 10 != 0