class Solution:
    def digitSum(self, s, k):
        
        # Lặp cho đến khi độ dài <= k
        while len(s) > k:
            new_s = ""
            
            # Chia chuỗi thành các nhóm độ dài k
            for i in range(0, len(s), k):
                group = s[i:i+k]
                
                # Tính tổng các chữ số trong nhóm
                total = sum(int(ch) for ch in group)
                
                # Nối vào chuỗi mới
                new_s += str(total)
            
            # Cập nhật lại s cho vòng tiếp theo
            s = new_s
        
        return s