class Node:
    def __init__(self):
        
        self.children={}
        self.isLast=False
class Trie:
    def __init__(self):
        self.root=Node()
        

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=Node()
            curr=curr.children[c]
        curr.isLast=True       


        

    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            if c not in curr.children:
                # curr.children[c]=Node()
                return False
            curr=curr.children[c]
        return curr.isLast
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            if c not in curr.children:
                # curr.children[c]=Node()
                return False
            curr=curr.children[c]
        # curr.isLast=True  
        return True
        