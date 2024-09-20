class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        self.cache = {n-1: cost[n-1], n-2: cost[n-2]}
        prices = []

        def helper(i, cost):
            if i in self.cache:
                return self.cache[i]

            
            self.cache[i] = cost[i] + min(helper(i+1, cost), helper(i+2, cost))
            
            return self.cache[i]

        return min(helper(0, cost), helper(1, cost))