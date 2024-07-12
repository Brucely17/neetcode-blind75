
class Node:
    def __init__(self):
        self.children={}
        self.isLast=False
class WordDictionary:

    def __init__(self):
        self.root=Node()
        

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word :
            if c not in curr.children:
                curr.children[c]=Node()
            curr=curr.children[c]
        curr.isLast=True

        

    def search(self, word: str) -> bool:
        # def dfs(root,i):
        #     if i==len(words):
        #         return True
        #     if word[i]=='.':
        #         for c in root.children:
        #             if dfs(root.children[c],i+1):
        #                 return True
        #         return False
        #     else:
        #         if word[i]!='.' and word[i] not in root.children:
        #             return False
        #         dfs(root.children[word[i]])

            
        curr=self.root
        j=0
        for c in range(len(word)):
            
            if word[c]=='.':
                for i in curr.children:
                    new=word[:c]+i+word[c+1:]
                    
                    if self.search(new):
                        
                        
                        return True
                return False
            else:
                if word[c] not in curr.children:
                    return False
                else:
                
                    curr=curr.children[word[c]]
        return curr.isLast
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



# //optimised

class Node:
    def __init__(self):
        self.children={}
        self.isLast=False
class WordDictionary:

    def __init__(self):
        self.root=Node()
        

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word :
            if c not in curr.children:
                curr.children[c]=Node()
            curr=curr.children[c]
        curr.isLast=True

        

    def search(self, word: str) -> bool:
        
        def dfs(i,root):
            
            curr=root
            
            for j in range(i,len(word)):
                c=word[j]
                if c=='.':
                    for child in curr.children.values():
                        
                        
                        if dfs(j+1,child):
                            
                            
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    
                    
                    curr=curr.children[c]
            return curr.isLast
        return dfs(0,self.root)
        

