class Solution {
    public boolean isValid(String s) {
        LinkedList<Character> stack = new LinkedList<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            char exp = '.';
            switch (c) {
                case '(':
                case '{':
                case '[':
                stack.addFirst(c);
                break;
                case ')':
                case '}':
                case ']':
                if (stack.isEmpty()) {
                    return false;
                }
                char el = stack.removeFirst();
                switch(c) {
                    case ')':
                    exp = '(';
                    break;
                    case '}':
                    exp = '{';
                    break;
                    case ']':
                    exp = '[';
                    break;
                }
                if (el != exp) {
                    return false;
                }

            }
        }
        return stack.isEmpty();
    }
}
