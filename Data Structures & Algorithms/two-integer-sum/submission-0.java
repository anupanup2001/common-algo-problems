class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> store = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            Integer diffIndex = store.getOrDefault(diff, null);
            if (diffIndex != null) {
                return new int[]{diffIndex, i};
            }
            store.put(nums[i], i);
        }
        return new int[]{-1, -1};
    }
}
