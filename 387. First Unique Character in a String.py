class Solution:
    def firstUniqChar(self, s):
        count = [0] * 26

        # Đếm số lần xuất hiện
        for c in s:
            count[ord(c) - ord('a')] += 1

        # Tìm ký tự đầu tiên xuất hiện đúng 1 lần
        for i in range(len(s)):
            if count[ord(s[i]) - ord('a')] == 1:
                return i

        return -1
