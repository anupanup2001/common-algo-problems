class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for (String str: strs) {
            encoded.append(str.length()).append(',').append(str);
        }
        return encoded.toString();
    }

    public List<String> decode(String str) {
        // s = 12,abcdefabcdef3,abc
        int i = 0;
        List<String> ret = new ArrayList<>();
        while (i < str.length()) {
            // Extract number;
            int beginIndex = i; // 0
            while (str.charAt(i) != ',') {
                i++;
                continue;               
            }   // i = 2;
            int len = Integer.valueOf(str.substring(beginIndex, i)); // 12
            i++; // 3
            
            // Word
            ret.add(str.substring(i, i + len)); 
            i = i + len; // 15 (3,abc)
        }
        return ret;
    }
}
