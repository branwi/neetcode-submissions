from functools import cache
class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        @cache
        def dfs(i, capacity):
            if i == len(profit):
                return 0
            if weight[i] > capacity:
                return dfs(i + 1,capacity)
            maxprofit = profit[i] + dfs(i + 1, capacity - weight[i])

            maxprofit = max(maxprofit, dfs(i + 1, capacity))
            return maxprofit
        
        return dfs(0, capacity)


            

        