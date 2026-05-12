class Solution:
    def removeDuplicates(self, nums):

        # Nếu mảng rỗng
        if not nums:
            return 0

        # i là vị trí lưu phần tử unique
        i = 0

        # j dùng để duyệt mảng từ phần tử thứ 2
        for j in range(1, len(nums)):

            # Nếu gặp phần tử khác nums[i]
            # nghĩa là tìm thấy số mới
            if nums[j] != nums[i]:

                # tăng vị trí lưu unique
                i += 1

                # gán số mới vào vị trí tiếp theo
                nums[i] = nums[j]

        # số lượng phần tử unique
        return i + 1