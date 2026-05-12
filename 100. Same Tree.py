class Solution(object):
    def isSameTree(self, p, q):
        # Nếu cả hai đều null → giống
        if not p and not q:
            return True
        
        # Nếu một null, một không → khác
        if not p or not q:
            return False
        
        # Nếu giá trị khác → khác
        if p.val != q.val:
            return False
        
        # So sánh tiếp trái và phải
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)