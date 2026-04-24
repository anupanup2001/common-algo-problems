class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> container = new HashSet<>();
        for (int num : nums) {
            if (container.contains(num)) {
                return true;
            }
            container.add(num);
        }
        return false;
    }
}