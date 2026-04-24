class Solution {
    public int countComponents(int n, int[][] edges) {
        List<List<Integer>> adj_list = new ArrayList();
        for (int i = 0; i < n; i++) {
            adj_list.add(new ArrayList<Integer>());
        }

        for (int[] edge : edges) {
            adj_list.get(edge[0]).add(edge[1]);
            adj_list.get(edge[1]).add(edge[0]);
        }

        Set<Integer> seen = new HashSet<>();
        int total_components = 0;
        for (int i = 0; i < n; i++) {
            if (seen.contains(i)) {
                continue;
            }
            total_components++;
            dfs(i, adj_list, seen);
        }
        return total_components;
    }

    void dfs(int i, List<List<Integer>> adj_list, Set<Integer> seen) {
        seen.add(i);
        for (int neighbor: adj_list.get(i)) {
            if (seen.contains(neighbor)) {
                continue;
            }
            dfs(neighbor, adj_list, seen);
        }
    }
}
