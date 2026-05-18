class Solution:
    def mostFrequent(self, nums, key):
        count = {}

        for i in range(len(nums) - 1):
            if nums[i] == key:
                target = nums[i + 1]
                if target in count:
                    count[target] += 1
                else:
                    count[target] = 1

        # tìm phần tử có count lớn nhất
        max_count = 0
        result = 0

        for k in count:
            if count[k] > max_count:
                max_count = count[k]
                result = k

        return result