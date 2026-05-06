class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1] * len(nums)
        after = [1] * len(nums)

        cum_result = 1
        for i in range(len(nums)):
            before[i] = cum_result
            cum_result *= nums[i]
        
        cum_result = 1
        for i in range(len(nums) - 1, -1, -1):
            after[i] = cum_result
            cum_result *= nums[i]
        
        # print(f'before = {before}, after = {after}')
        ans = []
        for b, a in zip(before, after):
            ans.append(b * a)
        return ans
