class Solution {
    int[][] seen;
    char[][] grid;
    int rows;
    int cols;
    public int numIslands(char[][] grid) {
        rows = grid.length;
        cols = grid[0].length;
        this.grid = grid;
        seen = new int[rows][cols];
        
        int num_islands = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (seen[i][j] == 1 || grid[i][j] == '0') {
                    continue;
                }
                num_islands++;
                dfs(i, j);
            }
        }
        return num_islands;
    }

    void dfs(int x, int y) {
        if (x < 0 || x >= rows) {
            return;
        }
        if (y < 0 || y >= cols) {
            return;
        }

        if (seen[x][y] == 1 || grid[x][y] == '0') {
            return;
        }
        seen[x][y] = 1;

        dfs(x, y + 1);
        dfs(x, y - 1);
        dfs(x + 1, y);
        dfs (x - 1, y);
    }
}
