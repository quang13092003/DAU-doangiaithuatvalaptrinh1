class Solution:
    def countHillValley(self, nums):
        # bước 1: loại phần tử trùng liên tiếp
        arr = [nums[0]]
        for x in nums[1:]:
            if x != arr[-1]:
                arr.append(x)

        count = 0

        # bước 2: đếm hill + valley
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                count += 1  # hill
            elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                count += 1  # valley

        return count