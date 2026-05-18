class Solution(object):
    def postorderTraversal(self, root):
        res = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)         # 1. Duyệt trái
            dfs(node.right)        # 2. Duyệt phải
            res.append(node.val)   # 3. Thăm node
        
        dfs(root)
        return res