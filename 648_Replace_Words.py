class Solution:
    
    class TrieNode:
        def __init__(self):
            self.is_word = False
            self.char_to_nodes = collections.defaultdict(Solution.TrieNode)
        
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        # Build Tree
        root = Solution.TrieNode()
        for word in dict:
            node = root
            for char in word:
                node = node.char_to_nodes[char]
            node.is_word = True

        new_list = []
        # Visit Tree
        for word in sentence.split(' '):
            node = root
            find_trie = False
            for i, char in enumerate(word, start=1):
                if char not in node.char_to_nodes:
                    break
                node = node.char_to_nodes[char]
                if node.is_word:
                    new_list.append(word[:i])
                    find_trie = True
                    break
            if not find_trie:
                new_list.append(word)
                
        return ' '.join(new_list)
        
