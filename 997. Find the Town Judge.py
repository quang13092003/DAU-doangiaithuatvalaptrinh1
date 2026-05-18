class Solution:
    def findJudge(self, n, trust):
        
        # Mảng đếm:
        # in_degree[i]: số người tin i
        # out_degree[i]: i tin bao nhiêu người
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)
        
        # Duyệt danh sách trust
        for a, b in trust:
            out_degree[a] += 1   # a tin người khác
            in_degree[b] += 1    # b được người khác tin
        
        # Judge phải:
        # - không tin ai -> out_degree = 0
        # - được n-1 người tin -> in_degree = n-1
        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i
        
        return -1