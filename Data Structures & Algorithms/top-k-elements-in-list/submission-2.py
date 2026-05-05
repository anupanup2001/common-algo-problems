from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        min_heap = []
        for val, count in freq.items():
            heapq.heappush(min_heap, (count, val))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        ans = [heapq.heappop(min_heap)[1] for _ in range(k)]
        return ans[::-1]