class Solution:
    def findCenter(self, edges):
        
        # Trong star graph:
        # Node trung tâm sẽ xuất hiện trong mọi cạnh
        
        # Chỉ cần lấy 2 cạnh đầu tiên:
        a, b = edges[0]
        c, d = edges[1]
        
        # Nếu a xuất hiện ở cạnh thứ 2 -> a là center
        if a == c or a == d:
            return a
        
        # Ngược lại b là center
        return b