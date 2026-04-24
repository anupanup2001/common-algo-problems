class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo1 = [-1] * len(nums)
        memo2 = [-1] * len(nums)
        def dfs(i, houses, memo):
            if i >= len(houses):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i + 1, houses, memo), houses[i] + dfs(i + 2, houses, memo))
            return memo[i]
        print(nums[:-1])
        rob = max(dfs(1, nums, memo1), dfs(0, nums[:-1], memo2))
        #print(memo)
        return rob