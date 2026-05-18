# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root):
        
        # Node giả để bắt đầu xây cây mới
        dummy = TreeNode(0)
        self.curr = dummy
        
        # Duyệt inorder (trái -> gốc -> phải)
        def inorder(node):
            # Nếu node rỗng -> dừng
            if not node:
                return
            
            # Duyệt trái
            inorder(node.left)
            
            # Xử lý node hiện tại:
            # - Bỏ left
            # - Gắn vào bên phải của curr
            node.left = None
            self.curr.right = node
            self.curr = node
            
            # Duyệt phải
            inorder(node.right)
        
        inorder(root)
        
        # Trả về cây mới (bỏ dummy)
        return dummy.right