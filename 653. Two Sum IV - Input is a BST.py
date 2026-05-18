# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root, k):
        
        # Dùng set để lưu các giá trị đã duyệt
        seen = set()
        
        def dfs(node):
            # Nếu node rỗng -> không tìm được
            if not node:
                return False
            
            # Nếu tồn tại số (k - node.val) trong set -> tìm thấy
            if (k - node.val) in seen:
                return True
            
            # Thêm giá trị hiện tại vào set
            seen.add(node.val)
            
            # Duyệt tiếp trái hoặc phải
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)