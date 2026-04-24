import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) >= 2:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)

            if stone1 == stone2:
                continue
            
            result = stone1 - stone2 if stone1 > stone2 else stone2 - stone1
            heapq.heappush(heap, -result)
        
        if len(heap) == 1:
            return -heap[0]
        return 0