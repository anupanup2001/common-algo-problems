class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> hashSet = new HashSet();
        for (int n: nums) {
            hashSet.add(n);
        }

        // Iterate the hashset 

        int runningSequence = 0;
        int maxSequence = 0;
        for (Integer n: hashSet) {
            runningSequence = 1;
            if (!hashSet.contains(n - 1)) {
                while (hashSet.contains(n + runningSequence)) {
                    runningSequence++;
                }
                maxSequence = Math.max(maxSequence, runningSequence);
            }
        }

        return maxSequence;
    }
}
