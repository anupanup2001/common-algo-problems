class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        match = {')': '(', ']' : '[', '}' : '{'}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                q.append(c)
            if c in match:
                if not q:
                    return False
                if match[c] != q.pop():
                    return False
        return len(q) == 0