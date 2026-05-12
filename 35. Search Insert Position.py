class Solution:
    def searchInsert(self, nums, target):

        # Con trỏ trái
        left = 0

        # Con trỏ phải
        right = len(nums) - 1

        # Chạy khi left chưa vượt right
        while left <= right:

            # Tìm vị trí giữa
            mid = (left + right) // 2

            # Nếu tìm thấy target
            if nums[mid] == target:
                return mid

            # Nếu target lớn hơn nums[mid]
            elif nums[mid] < target:

                # Tìm bên phải
                left = mid + 1

            else:
                # Tìm bên trái
                right = mid - 1

        # Nếu không tìm thấy
        # left chính là vị trí cần chèn
        return left