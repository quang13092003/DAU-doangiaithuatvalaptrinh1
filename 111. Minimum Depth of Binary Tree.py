class Solution(object):
    def minDepth(self, root):
        """
        Tìm độ sâu nhỏ nhất từ root đến leaf.
        Leaf = node không có con.
        """
        
        # Nếu cây rỗng → depth = 0
        if not root:
            return 0
        
        """
        Nếu 1 trong 2 nhánh bị thiếu:
        - Không được lấy min(left, right) vì sẽ ra 0 sai
        - Phải đi theo nhánh còn lại
        """
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        """
        Nếu có đủ 2 con:
        → lấy min depth của trái và phải
        """
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))