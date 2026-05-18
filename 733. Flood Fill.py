class Solution:
    def floodFill(self, image, sr, sc, color):
        
        rows = len(image)
        cols = len(image[0])
        
        # Màu gốc tại điểm bắt đầu
        original = image[sr][sc]
        
        # Nếu màu mới trùng màu cũ thì không cần làm gì
        if original == color:
            return image
        
        def dfs(r, c):
            # Nếu ra ngoài biên hoặc khác màu gốc thì dừng
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original:
                return
            
            # Tô màu mới
            image[r][c] = color
            
            # Lan sang 4 hướng
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        dfs(sr, sc)
        return image