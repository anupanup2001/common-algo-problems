import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        left = 0
        right = k - 1
        ans = []
        while right < len(nums):
            ans.append(-heap[0][0])
            left = left + 1
            right = right + 1
            
            if right < len(nums):
                heapq.heappush(heap, (-nums[right], right))
            while heap and heap[0][1] < left:
                heapq.heappop(heap)
        return ans