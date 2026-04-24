class PrefixTree:

    def __init__(self):
        self.map = {}
        self.end = False

    def insert(self, word: str) -> None:
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c not in curr.map:
                curr.map[c] = PrefixTree()
            curr = curr.map[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c not in curr.map:
                return False
            curr = curr.map[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for i in range(len(prefix)):
            c = prefix[i]
            if c not in curr.map:
                return False
            curr = curr.map[c]
        return True
        
        