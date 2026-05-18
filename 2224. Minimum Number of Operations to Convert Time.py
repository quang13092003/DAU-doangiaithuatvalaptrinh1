class Solution:
    def convertTime(self, current, correct):
        
        # Tách giờ và phút
        cur_h, cur_m = map(int, current.split(':'))
        cor_h, cor_m = map(int, correct.split(':'))
        
        # Đổi sang tổng số phút
        cur_total = cur_h * 60 + cur_m
        cor_total = cor_h * 60 + cor_m
        
        # Số phút cần tăng
        diff = cor_total - cur_total
        
        ops = 0
        
        # Dùng bước lớn trước để giảm số lần thao tác
        for step in [60, 15, 5, 1]:
            # Lấy được bao nhiêu lần step
            ops += diff // step
            
            # Cập nhật phần còn lại
            diff %= step
        
        return ops