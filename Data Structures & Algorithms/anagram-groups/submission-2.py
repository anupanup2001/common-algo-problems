from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_signature(s: str)->str:
            sig = [0]*26
            for c in s:
                sig[ord(c) - ord('a')] += 1
            return ",".join([str(val) for val in sig])
        
        sig_str = defaultdict(list)
        for string in strs:
            sig = get_signature(string)
            sig_str[sig].append(string)
        
        ans = []
        for group in sig_str.values():
            ans.append(group)
        return ans