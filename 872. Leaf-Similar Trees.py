# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1, root2):
        
        # Hàm lấy danh sách các lá theo thứ tự trái -> phải
        def getLeaves(node, leaves):
            # Nếu node rỗng -> bỏ qua
            if not node:
                return
            
            # Nếu là node lá -> thêm vào danh sách
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            
            # Duyệt trái rồi phải
            getLeaves(node.left, leaves)
            getLeaves(node.right, leaves)
        
        # Lấy danh sách lá của 2 cây
        leaves1 = []
        leaves2 = []
        
        getLeaves(root1, leaves1)
        getLeaves(root2, leaves2)
        
        # So sánh 2 danh sách
        return leaves1 == leaves2