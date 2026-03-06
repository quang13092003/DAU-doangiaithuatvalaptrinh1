class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        
        count = Counter(nums)                      # Đếm tần suất
        
        freq = [[] for _ in range(len(nums) + 1)]  # Bucket
        
        for num, c in count.items():
            freq[c].append(num)
        
        res = []
        # duyệt ngược từ tần suất lớn -> nhỏ
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
