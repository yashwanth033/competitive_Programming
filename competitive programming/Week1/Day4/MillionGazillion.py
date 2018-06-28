class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def search(self, key):

        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord

    def add_word(self, key):

        added = False
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                added = True
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        if not pCrawl.isEndOfWord:
            added = True
            pCrawl.isEndOfWord = True
        return added

if __name__ == '__main__':
    trie = Trie()

    print(trie.add_word('catch'))
    print(trie.add_word('cakes'))
    print(trie.add_word('cake'))
    print(trie.add_word('caked'))
    print(trie.add_word('catch'))
    print(trie.add_word(''))
    print(trie.add_word(''))
