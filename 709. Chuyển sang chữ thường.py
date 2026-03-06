class Solution(object):
    def toLowerCase(self, s):
        res = ""
        
        for c in s:
            if 'A' <= c <= 'Z':
                res += chr(ord(c) + 32)
            else:
                res += c
        
        return res