class Solution {
    public int characterReplacement(String s, int k) {
        int[] hash = new int[26];
        int retValue = 0;

        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            int currLen = right - left + 1;
            char c = s.charAt(right);
            hash[c - 'A']++;
            int maxCharFreq = maxCharFreq(hash);
            if (currLen - maxCharFreq <= k) {
                // Substr valid
                retValue = Math.max(retValue, currLen);
            } else {
                hash[s.charAt(left) - 'A']--;
                left++;
            }

        }

        return retValue;
    }

    private int maxCharFreq(int[] hash) {
        int max = 0;
        for (int count: hash) {
            max = Math.max(max, count);
        }
        return max;
    }
}
