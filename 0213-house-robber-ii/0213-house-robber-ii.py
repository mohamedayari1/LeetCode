class Solution:
    def rob(self, nums: List[int]) -> int:    
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[: len(nums)-1]))
    
    def helper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = rob2
            rob2 = max(rob2, rob1 + n)
            rob1 = tmp
        return rob2