from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append((v, t))
        
        minHeap = [(0, k)]

        visit = set()

        result = 0
        
        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            result = max(result, t)
            for n1, t1 in edges[node]:
                if n1 in visit:
                    continue
                heapq.heappush(minHeap, (t + t1, n1))
        return result if len(visit) == n else -1

