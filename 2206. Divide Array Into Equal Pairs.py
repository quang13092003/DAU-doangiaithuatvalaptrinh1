class Solution:
    def divideArray(self, nums):
        count = {}

        # đếm số lần xuất hiện
        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1

        # kiểm tra chẵn/lẻ
        for x in count:
            if count[x] % 2 != 0:
                return False

        return True