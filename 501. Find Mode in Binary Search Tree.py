# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root):
        
        # Dùng inorder để duyệt BST theo thứ tự tăng dần
        self.prev = None          # Lưu giá trị trước đó
        self.count = 0            # Đếm số lần xuất hiện hiện tại
        self.max_count = 0        # Tần suất lớn nhất
        self.result = []          # Danh sách mode
        
        def inorder(node):
            if not node:
                return
            
            # Duyệt trái
            inorder(node.left)
            
            # Nếu giá trị giống trước đó -> tăng count
            # Ngược lại reset count = 1
            if self.prev == node.val:
                self.count += 1
            else:
                self.count = 1
            
            # Nếu count > max_count -> cập nhật result mới
            if self.count > self.max_count:
                self.max_count = self.count
                self.result = [node.val]
            
            # Nếu count == max_count -> thêm vào result
            elif self.count == self.max_count:
                self.result.append(node.val)
            
            # Cập nhật prev
            self.prev = node.val
            
            # Duyệt phải
            inorder(node.right)
        
        inorder(root)
        return self.result