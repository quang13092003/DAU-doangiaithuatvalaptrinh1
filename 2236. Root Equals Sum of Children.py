# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkTree(self, root):
        
        # Vì đề bài đảm bảo có đúng 3 node:
        # root, root.left, root.right
        
        # So sánh giá trị root với tổng 2 node con
        return root.val == root.left.val + root.right.val