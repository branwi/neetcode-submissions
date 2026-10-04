class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_profit = 0
        buy = prices[i]
        while i < len(prices):
            if prices[i] > buy:
                max_profit = max(max_profit, prices[i] - buy)
            else:
                buy = prices[i]
            i+=1
        return max_profit