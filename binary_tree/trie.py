class Trie:
    def __init__(self):
        # Root node is an empty dictionary
        self.root = {}

    def insert(self, word):
        """
        Insert a word into the Trie.
        """
        current = self.root
        for char in word:
            # Add the character to the dictionary if it doesn't exist
            if char not in current:
                current[char] = {}
            # Move to the next node
            current = current[char]
        # Mark the end of the word
        current['*'] = True

    def search(self, word):
        """
        Search for a word in the Trie.
        Returns True if the word exists, False otherwise.
        """
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        # Check if the end-of-word marker is present
        return '*' in current

    def starts_with(self, prefix):
        """
        Check if there is any word in the Trie that starts with the given prefix.
        """
        current = self.root
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True

if __name__ == '__main__':
    # Initialize Trie
    trie = Trie()

    # Insert words
    trie.insert("apple")
    trie.insert("app")

    # Search for words
    print(trie.search("apple"))  # True
    print(trie.search("app"))  # True
    print(trie.search("appl"))  # False

    # Check prefixes
    print(trie.starts_with("app"))  # True
    print(trie.starts_with("apx"))  # False
