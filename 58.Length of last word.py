class Solution:
    def lengthOfLastWord(self, s):
        length = 0
        i = len(s) - 1

        # Bỏ các dấu cách ở cuối
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Đếm độ dài từ cuối cùng
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length
