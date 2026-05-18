class Solution(object):
    def secondHighest(self, s):
        digits = set()

        for c in s:
            if c.isdigit():
                digits.add(int(c))

        if len(digits) < 2:
            return -1

        digits = sorted(digits, reverse=True)
        return digits[1]