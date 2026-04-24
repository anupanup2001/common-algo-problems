class Solution {
    public boolean isAnagram(String s, String t) {
        int length = s.length();
        
        // Not equal
        if (length != t.length()) {
            return false;
        }

        Map<Character, Integer> container = new HashMap<>();
        for (char c : s.toCharArray()) {
            int currCount = container.getOrDefault(c, 0);
            currCount++;
            container.put(c, currCount);
        }

        for (char c : t.toCharArray()) {
            int currCount = container.getOrDefault(c, 0);
            currCount --;
            if (currCount < 0) {
                return false;
            }
            container.put(c, currCount);
        }
        return true;
    }
}
