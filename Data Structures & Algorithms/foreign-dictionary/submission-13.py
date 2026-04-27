from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj = defaultdict(set)
        indegree = {c: 0 for w in words for c in w}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return ""
            for c1, c2 in zip(word1, word2):
              
                if c1 == c2:
                    continue
                if c2 not in adj[c1]:
                    indegree[c2] += 1
                adj[c1].add(c2)
                

                break
        
        print(adj)
        print(indegree)
        # Kahns topological sort
        q = deque()
        for c, v in indegree.items():
            if v == 0:
                q.append(c)
        
        seen = set()
        ans = ''
        while q:
            c = q.popleft()
            if c in seen:
                continue
            ans += c
            for neighbor in adj[c]:
                if neighbor in seen:
                    continue
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return ans if len(ans) == len(indegree) else ""