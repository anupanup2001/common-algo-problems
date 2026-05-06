class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for s in strs:
            out += f"{len(s)}:{s}"
        return out

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            # Find the length of the first string
            idx = s.find(':', i, len(s))
            if idx != -1:
                length = int(s[i:idx])
                print(f'len = {length}')
                ans.append(s[idx + 1: idx + 1 + length])
            i = idx + 1 + length
        return ans