class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        right = 0
        window = set()
        while right < len(s):
            # Expand the window
            c = s[right]
            if c in window:
                # Move left till the existing c is removed
                while s[left] != c:
                    window.remove(s[left])
                    left += 1
                window.remove(s[left])
                left += 1
            
            # c is not in window now
            window.add(c)
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len