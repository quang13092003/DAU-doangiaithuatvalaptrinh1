class Solution:
    def majorityElement(self, nums):
        
        # Boyer-Moore Voting Algorithm
        candidate = None
        count = 0
        
        for num in nums:
            # Nếu count = 0 -> chọn candidate mới
            if count == 0:
                candidate = num
            
            # Nếu giống candidate -> tăng
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        # Candidate cuối cùng chính là majority element
        return candidate