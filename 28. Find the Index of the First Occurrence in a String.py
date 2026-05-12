class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Độ dài chuỗi lớn
        n = len(haystack)

        # Độ dài chuỗi cần tìm
        m = len(needle)

        # Duyệt từng vị trí có thể bắt đầu
        # n - m + 1 để không bị vượt giới hạn
        for i in range(n - m + 1):

            # Cắt chuỗi từ i đến i + m
            # rồi so sánh với needle
            if haystack[i:i + m] == needle:

                # Nếu giống thì trả về vị trí
                return i

        # Không tìm thấy
        return -1