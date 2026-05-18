class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        
        # Đảo left và right
        root.left, root.right = root.right, root.left
        
        # Đệ quy xuống hai nhánh
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root