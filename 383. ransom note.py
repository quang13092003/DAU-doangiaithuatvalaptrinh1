class Solution:
    def canConstruct(self, ransomNote, magazine):
        count = [0] * 26

        for ch in magazine:
            count[ord(ch) - ord('a')] += 1

        for ch in ransomNote:
            idx = ord(ch) - ord('a')
            if count[idx] == 0:
                return False
            count[idx] -= 1

        return True