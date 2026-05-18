class Solution:
    def isBoomerang(self, points):
        
        # Lấy 3 điểm
        (x1, y1), (x2, y2), (x3, y3) = points
        
        # Kiểm tra không thẳng hàng:
        # Diện tích tam giác != 0
        # (x2-x1)*(y3-y1) != (x3-x1)*(y2-y1)
        
        return (x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1)