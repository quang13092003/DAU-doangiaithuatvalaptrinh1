import heapq
import math

class Solution:
    def pickGifts(self, gifts, k):
        # tạo max heap (dùng số âm)
        heap = [-x for x in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            x = -heapq.heappop(heap)   # lấy số lớn nhất
            x = int(math.sqrt(x))      # lấy căn bậc 2 (floor)
            heapq.heappush(heap, -x)

        return -sum(heap)