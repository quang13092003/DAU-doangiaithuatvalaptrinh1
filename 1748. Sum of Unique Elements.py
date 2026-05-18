class Solution(object):
    def sumOfUnique(self, nums):
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        result = 0
        for n in count:
            if count[n] == 1:
                result += n

        return result