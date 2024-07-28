class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return 

            # Choice of adding the next element
            subset.append(nums[i])
            dfs(i+1)
            

            # Choice of not adding the next element
            subset.pop()
            dfs(i+1)

        dfs(0)
        return result