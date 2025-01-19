class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # result = nums
        # return result.extend(nums)

        n = len(nums) 
        result = [0] * 2 * n

        for i, num in enumerate(nums):
            result[i], result[i+n] = num, num

        return result