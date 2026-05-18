class Solution:
    def isPalindrome(self, s):
        filtered = ""

        for c in s:
            if c.isalnum():
                filtered += c.lower()

        return filtered == filtered[::-1]