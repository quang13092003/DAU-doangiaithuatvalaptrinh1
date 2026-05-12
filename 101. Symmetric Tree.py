class Solution:
    def isSymmetric(self, root):

        # Hàm kiểm tra 2 cây có đối xứng không
        def isMirror(left, right):

            # Nếu cả 2 đều rỗng
            if not left and not right:
                return True

            # Nếu 1 bên rỗng
            if not left or not right:
                return False

            # Nếu giá trị khác nhau
            if left.val != right.val:
                return False

            # Kiểm tra đối xứng tiếp
            return (
                isMirror(left.left, right.right)
                and
                isMirror(left.right, right.left)
            )

        # So sánh cây trái và cây phải
        return isMirror(root.left, root.right)