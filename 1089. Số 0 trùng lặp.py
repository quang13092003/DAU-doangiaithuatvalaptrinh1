class Solution(object):
    def duplicateZeros(self, arr):
        res = []
        
        for num in arr:
            if num == 0:
                res.append(0)
                res.append(0)
            else:
                res.append(num)
        
        for i in range(len(arr)):
            arr[i] = res[i]