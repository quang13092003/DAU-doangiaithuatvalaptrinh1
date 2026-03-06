class Solution:
    def plusOne(self, digits):
        n = len(digits)

        # Duyệt từ cuối mảng về đầu
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # Nếu tất cả đều là 9 (ví dụ: [9], [9,9,9])
        return [1] + digits
