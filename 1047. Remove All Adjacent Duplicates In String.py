class Solution:
    def removeDuplicates(self, s):
        stack = []

        for c in s:
            if stack and stack[-1] == c:
                stack.pop()   # xóa cặp trùng
            else:
                stack.append(c)

        return "".join(stack)