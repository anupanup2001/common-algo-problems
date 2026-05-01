from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dfs(idx):
            if idx >= len(nums):
                return 0
            return max(dfs(idx + 1), nums[idx] + dfs(idx + 2))
        return dfs(0)
            