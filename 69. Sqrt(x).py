class Solution:
    def mySqrt(self, x):

        # Biên trái
        left = 0

        # Biên phải
        right = x

        # Lưu đáp án gần đúng nhất
        ans = 0

        # Binary Search
        while left <= right:

            # Tìm vị trí giữa
            mid = (left + right) // 2

            # Nếu mid^2 <= x
            # nghĩa là mid có thể là đáp án
            if mid * mid <= x:

                # Lưu đáp án
                ans = mid

                # Thử tìm số lớn hơn
                left = mid + 1

            else:
                # mid quá lớn
                # tìm bên trái
                right = mid - 1

        # Trả về căn bậc hai nguyên
        return ans