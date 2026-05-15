class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def recur(list_nums, curr_sum, idx):
            if curr_sum == target:
                ans.append(list_nums.copy())
                return
            
            if curr_sum > target:
                return
            
            if idx >= len(nums):
                return
            while idx < len(nums):
                num = nums[idx]
                list_nums.append(num)
                recur(list_nums, curr_sum + num, idx)
                list_nums.pop()
                idx += 1
        recur([], 0, 0)
        return ans