class Solution {
    public int maxArea(int[] heights) {
        int maxVolume = 0;
        int left = 0;
        int right = heights.length - 1;
        while (left < right) {
            int volume = (right - left) * Math.min(heights[left], heights[right]);
            maxVolume = Math.max(maxVolume, volume);
            if (heights[left] < heights[right]) {
                // Move left to a bigger bar to the right
                int currHeight = heights[left];
                while (left < right && heights[left] <= currHeight) {
                    left++;
                }
            } else {
                // Move right to a bigger bar to the left
                int currHeight = heights[right];
                while (left < right && heights[right] <= currHeight) {
                    right--;
                }
            }
        }

        return maxVolume;
    }
}
