from collections import defaultdict
import heapq

class Solution:
    

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)

        adj = defaultdict(set)
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                adj[i].add((j, dist(points[i], points[j])))
                adj[j].add((i, dist(points[i], points[j])))
        # print(adj)
        
        visited = set()
        total_dist = 0
        q = [(0, 0)]
        nodes = 0
        while q:
            dist, point = heapq.heappop(q)
            if point in visited:
                continue
            total_dist += dist
            visited.add(point)
            nodes += 1
            # print(f"node={point}, total_dist={total_dist}")
            if nodes == len(points):
                break
            for neighbor, d in adj[point]:
                if neighbor not in visited:
                    heapq.heappush(q, (d, neighbor))
        
        return total_dist
