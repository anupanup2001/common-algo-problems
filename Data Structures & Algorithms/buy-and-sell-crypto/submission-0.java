class Solution {
    public int maxProfit(int[] prices) {
        int maxTillNow = 0;
        // find the buy point
        int maxProfit = 0;
        for (int i = prices.length - 1; i >= 0; i--) {
            int profit = maxTillNow - prices[i];
            maxProfit = Math.max(maxProfit, profit);
            maxTillNow = Math.max(maxTillNow, prices[i]);
        }
        return maxProfit;
    }
}
