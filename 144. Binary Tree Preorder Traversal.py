class Solution(object):
    def preorderTraversal(self, root):
        res = []
        
        def dfs(node):
            if not node:
                return
            
            res.append(node.val)   # 1. Thăm node hiện tại
            dfs(node.left)         # 2. Duyệt cây con trái
            dfs(node.right)        # 3. Duyệt cây con phải
        
        dfs(root)
        return res