class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        seen = set()

        for i, num in enumerate(nums):
            tmp = target - num
            if num in seen:
                return [i, num_to_index[num]]

            num_to_index[tmp] = i
            seen.add(tmp)