class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        r = len(heights)
        c = len(heights[0])
        pacific = [[0] * c for _ in range(r)]
        atlantic = [[0] * c for _ in range(r)]
        
        def dfs(ocean, isPacific):
            direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            q = deque()
            if isPacific:
                for i in range(c):
                    q.append([0, i])
                for i in range(r):
                    q.append([i, 0])
            else:
                for i in range(c):
                    q.append([r - 1, i])
                for i in range(r):
                    q.append([i, c - 1])
            
            while q:
                el = q.popleft()
                i = el[0]
                j = el[1]
                ocean[i][j] = 1
                for d in direction:
                    x = i + d[0]
                    y = j + d[1]
                    if x < 0 or y < 0 or x >= r or y >= c:
                        continue
                    if heights[x][y] >= heights[i][j] and ocean[x][y] == 0:
                        q.append([x, y])
        dfs(pacific, True)
        dfs(atlantic, False)

        ans = []
        for i in range(r):
            for j in range(c):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    ans.append([i, j])
        return ans