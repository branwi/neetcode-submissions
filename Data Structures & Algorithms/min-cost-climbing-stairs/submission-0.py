class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        stairs = [0] * len(cost)
        stairs[0] = cost[0]
        stairs[1] = cost[1]
        for i in range(2, len(cost)):
            stairs[i] = cost[i] + min(stairs[i-1], stairs[i-2])
        
        return min(stairs[-1], stairs[-2])