class Solution:
    def countEven(self, num):
        count = 0

        for i in range(1, num + 1):
            s = 0
            x = i

            # tính tổng chữ số
            while x > 0:
                s += x % 10
                x //= 10

            if s % 2 == 0:
                count += 1

        return count