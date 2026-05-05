class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_idx = {}
        for i, val in enumerate(nums):
            if target - val in value_idx:
                return [value_idx[target - val], i]
            value_idx[val] = i
        return [0, 0]