# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isUnivalTree(self, root):
        
        # Lưu giá trị gốc để so sánh
        value = root.val
        
        def dfs(node):
            # Nếu node rỗng -> đúng
            if not node:
                return True
            
            # Nếu giá trị khác root -> sai
            if node.val != value:
                return False
            
            # Kiểm tra tiếp trái và phải
            return dfs(node.left) and dfs(node.right)
        
        return dfs(root)