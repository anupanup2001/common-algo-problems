class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> store = new HashMap<>();
        for (int num: nums) {
            int currCount = store.getOrDefault(num, 0);
            currCount++;
            store.put(num, currCount);
        }

        PriorityQueue<Pair<Integer, Integer>> queue = new PriorityQueue<>((x, y) -> y.getValue() - x.getValue());
        store.forEach((key, value) -> queue.add(new Pair(key, value)));
        int[] ret = new int[k];
        for (int i = 0; i < k; i++) {
            ret[i] = queue.poll().getKey();
        }
        return ret;

    }
}
