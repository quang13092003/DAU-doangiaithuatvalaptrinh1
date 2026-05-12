class Solution:
    def removeElement(self, nums, val):

        # i là vị trí để ghi phần tử hợp lệ
        i = 0

        # j dùng để duyệt toàn bộ mảng
        for j in range(len(nums)):

            # Nếu phần tử hiện tại KHÔNG phải val
            if nums[j] != val:

                # Ghi phần tử đó vào vị trí i
                nums[i] = nums[j]

                # Tăng i để chuẩn bị ghi phần tử tiếp theo
                i += 1

        # i chính là số phần tử còn lại
        return i