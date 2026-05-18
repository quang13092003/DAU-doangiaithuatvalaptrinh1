class Solution(object):
    def binaryTreePaths(self, root):
        res = []
        
        def dfs(node, path):
            if not node:
                return
            
            # Nếu là node lá
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return
            
            # Đi tiếp xuống trái và phải
            dfs(node.left, path + str(node.val) + "->")
            dfs(node.right, path + str(node.val) + "->")
        
        dfs(root, "")
        return res