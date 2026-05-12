class Solution:
    def climbStairs(self, n):

        # Nếu n = 1
        if n == 1:
            return 1

        # a = số cách tới bậc 1
        # b = số cách tới bậc 2
        a = 1
        b = 2

        # Tính từ bậc 3 -> n
        for i in range(3, n + 1):

            # số cách hiện tại
            c = a + b

            # cập nhật
            a = b
            b = c

        return b