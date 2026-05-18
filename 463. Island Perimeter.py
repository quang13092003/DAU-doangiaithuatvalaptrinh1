class Solution:
    def islandPerimeter(self, grid):
        
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        # Duyệt từng ô trong grid
        for i in range(rows):
            for j in range(cols):
                
                # Nếu là đất
                if grid[i][j] == 1:
                    # Mỗi ô đất có tối đa 4 cạnh
                    perimeter += 4
                    
                    # Nếu phía trên cũng là đất -> trừ 2 cạnh chung
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    
                    # Nếu bên trái cũng là đất -> trừ 2 cạnh chung
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        
        return perimeter