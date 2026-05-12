class Solution:
    def inorderTraversal(self, root):

        # List lưu kết quả
        result = []

        # Hàm DFS đệ quy
        def dfs(node):

            # Nếu node rỗng thì dừng
            if not node:
                return

            # Duyệt cây con bên trái
            dfs(node.left)

            # Thêm node hiện tại vào result
            result.append(node.val)

            # Duyệt cây con bên phải
            dfs(node.right)

        # Bắt đầu từ root
        dfs(root)

        # Trả về kết quả
        return result