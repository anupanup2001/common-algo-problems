class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s2.length() < s1.length()) {
            return false;
        }
        int left = 0;
        int right = s1.length(); // 3

        String s1Sig = getFreqSignature(s1);
        System.out.println(s1Sig);
        while (right <= s2.length()) {
            String subStrSig = getFreqSignature(s2.substring(left, right));
            System.out.println(subStrSig);
            if (s1Sig.equals(subStrSig)) {
                return true;
            }
            left++;
            right++;
        }
        return false;
    }

    private String getFreqSignature(String s) {
        int[] hash = new int[26];
        s.chars().forEach(c -> hash[c - 'a']++);

        StringBuilder str = new StringBuilder();
        for(int x : hash) {
            str.append(x).append(':');
        }
        return str.toString();
    }
}
