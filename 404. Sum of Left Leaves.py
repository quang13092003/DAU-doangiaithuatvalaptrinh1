# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root):
        
        # Hàm DFS để duyệt cây
        def dfs(node, is_left):
            # Nếu node rỗng thì không cộng gì
            if not node:
                return 0
            
            # Nếu là node lá (không có con trái/phải)
            # và là lá bên trái -> cộng giá trị
            if not node.left and not node.right:
                return node.val if is_left else 0
            
            # Gọi đệ quy:
            # node.left -> là lá bên trái => True
            # node.right -> không phải bên trái => False
            return dfs(node.left, True) + dfs(node.right, False)
        
        # Bắt đầu từ root, root không phải là lá bên trái
        return dfs(root, False)