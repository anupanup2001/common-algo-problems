class Solution {
    public boolean isPalindrome(String s) {
        String sanitizedString = this.sanitizeString(s);
        System.out.println(sanitizedString);
        int left = 0;
        int right = sanitizedString.length() - 1;
        while (left < right) {
            if (sanitizedString.charAt(left) != sanitizedString.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    private String sanitizeString(String s) {
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isUpperCase(c)) {
                c = Character.toLowerCase(c);
            }

            if ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9')) {
                str.append(c);
            }
        }
        return str.toString();
    }
}
