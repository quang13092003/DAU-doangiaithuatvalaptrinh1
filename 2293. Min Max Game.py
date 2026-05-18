class Solution:
    def minMaxGame(self, nums):
        
        # Lặp cho đến khi còn 1 phần tử
        while len(nums) > 1:
            new_nums = []
            n = len(nums)
            
            # Tạo mảng mới theo quy tắc
            for i in range(n // 2):
                
                # Nếu i chẵn -> lấy min
                if i % 2 == 0:
                    new_nums.append(min(nums[2*i], nums[2*i + 1]))
                
                # Nếu i lẻ -> lấy max
                else:
                    new_nums.append(max(nums[2*i], nums[2*i + 1]))
            
            # Cập nhật nums
            nums = new_nums
        
        return nums[0]