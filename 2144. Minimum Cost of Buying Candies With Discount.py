class Solution:
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        total = 0
        
        for i in range(len(cost)):
            # Skip every 3rd candy (free one)
            if (i + 1) % 3 != 0:
                total += cost[i]
        
        return total