class Solution:
    def moveZeroes(self, nums):
        k = 0  # vị trí đặt số khác 0

        # đưa số khác 0 lên đầu
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1

        # fill 0 phía sau
        for i in range(k, len(nums)):
            nums[i] = 0