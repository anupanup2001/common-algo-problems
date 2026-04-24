class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<String>> store = new HashMap<>();
        for (String str: strs) {
            String sig = this.getAnagramSignature(str);
            if (store.get(sig) == null) {
                store.put(sig, new ArrayList<String>());
            }
            ArrayList<String> group = store.get(sig);
            group.add(str);
        }

        List<List<String>> retValue = new ArrayList<>();
        for (List<String> value : store.values()) {
            retValue.add(value);
        }
        return retValue;

    }

    private String getAnagramSignature(String str) {
        int[] hash = new int[26];
        for (int i = 0; i < str.length(); i++) {
            hash[str.charAt(i) - 'a']++;
        }
        String ret = "";
        for (int i: hash) {
            ret = ret + String.valueOf(i) + ':';
        }
        return ret;
    }
}
