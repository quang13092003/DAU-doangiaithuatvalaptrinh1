class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        Kiểm tra có tồn tại đường đi từ root → leaf
        sao cho tổng các node = targetSum
        """
        
        # Nếu cây rỗng → không có đường đi
        if not root:
            return False
        
        """
        Nếu là leaf:
        - Không có left và right
        - So sánh giá trị còn lại
        """
        if not root.left and not root.right:
            return targetSum == root.val
        
        """
        Trừ dần giá trị node hiện tại khỏi target
        rồi kiểm tra xuống 2 nhánh
        """
        remaining = targetSum - root.val
        
        return (
            self.hasPathSum(root.left, remaining) or
            self.hasPathSum(root.right, remaining)
        )