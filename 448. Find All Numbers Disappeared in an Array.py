class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        # Đánh dấu các số đã xuất hiện
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Thu thập các số chưa xuất hiện
        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result
