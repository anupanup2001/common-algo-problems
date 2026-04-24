class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def search(self, word: str) -> bool:
        if not word:
            return self.endOfWord
        c = word[0]

        if c not in self.children and c != '.':
            return False
        if c != '.':
            return self.children[c].search(word[1:])
        
        for child in self.children.values():
            if child.search(word[1:]):
                return True
        return False
class WordDictionary:

    def __init__(self):
        self.root = Trie()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        return self.root.search(word)
        
