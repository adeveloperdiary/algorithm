from collections import defaultdict


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = defaultdict(TrieNode)

    ## Initialize this node in the Trie
    def insert(self, char):
        self.children[char] = TrieNode()

    def find(self, node, word):
        arr = []

        for key in node.children:
            arr.extend(self.find(node.children[key], word + key))

        if node.is_word:
            arr.append(word)

        return arr

    def suffixes(self, suffix=''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point

        arr = []

        for key in self.children:
            arr.extend(self.find(self.children[key], key))

        return arr


## Add a child node in this Tri

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    ## Initialize this Trie (add a root node)

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for w in word:
            # node.insert(w)
            node = node.children[w]
        node.is_word = True

    def find(self, prefix):
        node = self.root

        match = False

        for p in prefix:
            if p in node.children:
                match = True
                node = node.children[p]

        if match:
            return node
        else:
            return ''


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


f('a')
f('fri')
