class Solution:
    def helper(self, i, nums, subsets, cur_set):
         
        if i >= len(nums):
            subsets.append(cur_set.copy())
            return 
        
        cur_set.append(nums[i])
        self.helper(i+1, nums, subsets, cur_set)

        cur_set.pop()
        self.helper(i+1, nums, subsets, cur_set)


    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, cur_set = [], []
        self.helper(0, nums, subsets, cur_set)
        return subsets