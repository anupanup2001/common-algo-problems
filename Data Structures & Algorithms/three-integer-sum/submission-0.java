class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        // [-4, -1, -1, 0, 1, 2]
        //   i               r
        List<List<Integer>> triplets = new ArrayList();
        for (int i = 0; i < nums.length - 2; i++) {
            int left = i + 1;
            int right = nums.length - 1;
            int target = -nums[i]; // 4
            while (left < right) {
                int sum = nums[left] + nums[right]; // 1
                if (sum < target) {
                    left++;
                } else if (sum > target) {
                    right--;
                } else {
                    triplets.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    // Move ahead of duplicates
                    while (left < right && nums[left] == nums[left + 1]) {
                        left++;
                    }

                    while (left < right && nums[right] == nums[right - 1]) {
                        right--;
                    }

                    left++;
                    right--;
                }
            }
            // Skip duplicates
            while (i < nums.length - 2 && nums[i] == nums[i + 1]) {
                i++;
            }
        }

        return triplets;
    }
}
