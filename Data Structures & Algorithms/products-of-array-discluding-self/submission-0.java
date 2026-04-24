class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefixProduct = new int[nums.length];
        int[] suffixProduct = new int[nums.length];

        int runningProduct = 1;
        // prefix
        for (int i = 0; i < nums.length; i++) {
            prefixProduct[i] = runningProduct;
            runningProduct = runningProduct * nums[i];
        }

        runningProduct = 1;
        // suffix
        for (int i = nums.length - 1; i >= 0; i--) {
            suffixProduct[i] = runningProduct;
            runningProduct = runningProduct * nums[i];
        }

        int[] retArray = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            retArray[i] = prefixProduct[i] * suffixProduct[i];
        }
        return retArray;
    }
}  
