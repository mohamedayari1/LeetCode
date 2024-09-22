class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        # cache = {n-1: cost[n-1], n-2: cost[n-2]}
        # def helper(i, cache):
        #     if i in cache:
        #         return cache[i]
        #     cache[i] = cost[i] + min(helper(i+1, cache), helper(i+2, cache))
            
        #     return cache[i] 


        # return min(helper(0, cache), helper(1, cache))

        for i in range(n-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])