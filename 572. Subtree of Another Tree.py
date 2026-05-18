class Solution:
    def isSubtree(self, root, subRoot):
        
        def isSameTree(a, b):
            # Nếu cả hai đều rỗng → giống nhau
            if not a and not b:
                return True
            
            # Nếu một trong hai rỗng → không giống
            if not a or not b:
                return False
            
            # Nếu giá trị node khác nhau → không giống
            if a.val != b.val:
                return False
            
            # So sánh tiếp trái và phải
            return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
        
        # Nếu root rỗng → không thể chứa subRoot
        if not root:
            return False
        
        # Nếu tại node hiện tại mà 2 cây giống nhau → return True
        if isSameTree(root, subRoot):
            return True
        
        # Ngược lại, thử ở cây con trái hoặc phải
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)