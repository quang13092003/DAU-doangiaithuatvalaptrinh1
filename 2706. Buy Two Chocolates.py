class Solution:
    def buyChoco(self, prices, money):
        
        # Tìm 2 giá nhỏ nhất
        prices.sort()
        
        cost = prices[0] + prices[1]
        
        # Nếu đủ tiền mua
        if cost <= money:
            return money - cost
        
        # Không đủ tiền -> giữ nguyên
        return money