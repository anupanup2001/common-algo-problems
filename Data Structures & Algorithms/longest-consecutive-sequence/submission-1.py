class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        contains = set()
        for num in nums:
            contains.add(num)
        
        max_seq = 0
        for num in contains:
            if num - 1 in contains:
                continue
            curr_seq = 1
            while num + curr_seq in contains:
                curr_seq += 1
            max_seq = max(max_seq, curr_seq)
        return max_seq