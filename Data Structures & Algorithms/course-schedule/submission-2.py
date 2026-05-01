from collections import defaultdict
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = defaultdict(set)
        for pre, post in prerequisites:
            adj[pre].add(post)
            indegree[post]+= 1
        
        # Kahns sort
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        ans = []
        seen = set()
        while (q):
            node = q.popleft()
            if node in seen:
                continue
            ans.append(node)
            for neighbor in adj[node]:
                if neighbor in seen:
                    continue
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return len(ans) == numCourses