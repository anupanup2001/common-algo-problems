class Solution {
    public boolean exist(char[][] board, String word) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (dfs(board, i, j, 0, word)) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean dfs(char[][] board, int i, int j, int k, String target){
        if (k == target.length()) {
            return true;
        }
        
        if (i < 0 || j < 0 || i >= board.length || j >= board[0].length || board[i][j] == '#') {
            return false;
        }

        

        if (board[i][j] != target.charAt(k)) {
            return false;
        }

        k = k + 1;
        board[i][j] = '#';
        boolean ret = dfs(board, i + 1, j, k, target) ||
            dfs(board, i - 1, j, k, target) ||
            dfs(board, i, j + 1, k, target) ||
            dfs(board, i, j - 1, k, target);
        board[i][j] = target.charAt(k-1);
        return ret;
    }
}
