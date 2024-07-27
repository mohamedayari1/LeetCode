class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.seen = set()

    def insert(self, word: str) -> None:

        self.seen.add(word)
        
        list_of_characters = list(word)
        
        current_node = self.root
        
        for c in list_of_characters:
            if c in current_node.children:
                current_node = current_node.children[c]
                
            else:
                new_node = TrieNode()
                current_node.children[c] = new_node
                current_node = new_node


    def search(self, word: str) -> bool:
        return word in self.seen
        
    def startsWith(self, prefix: str) -> bool:
        result = True
        list_of_characters = list(prefix)
        
        current_node = self.root

        for c in list_of_characters:
            if c in current_node.children:
                current_node = current_node.children[c]
                
            else:
                result = False
                break
        return result

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)