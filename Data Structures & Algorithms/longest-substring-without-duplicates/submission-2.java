class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) {
            return 0;
        }
        
        Map<Character, Integer> charToIndex = new HashMap();
        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            if (charToIndex.containsKey(s.charAt(right))) {
                left = Math.max(left, charToIndex.get(s.charAt(right)) + 1);
            }
            charToIndex.put(s.charAt(right), right);
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
}
// public class Solution {
//     public int lengthOfLongestSubstring(String s) {
//         HashMap<Character, Integer> mp = new HashMap<>();
//         int l = 0, res = 0;

//         for (int r = 0; r < s.length(); r++) {
//             if (mp.containsKey(s.charAt(r))) {
//                 l = Math.max(mp.get(s.charAt(r)) + 1, l);
//             }
//             mp.put(s.charAt(r), r);
//             res = Math.max(res, r - l + 1);
//         }
//         return res;
//     }
// }