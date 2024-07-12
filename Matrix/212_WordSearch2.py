board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
word=words[1]
board = [["a","b"],["c","d"]]
words = ["abcb"]
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Node:
            def __init__(self):
                self.children={}
                self.isLast=False
        
        class Trie:
            def __init__(self):
                self.root=Node()
            def insert(self,word):
                
                curr=self.root
                
                for c in word:
                    if c not in curr.children:
                        curr.children[c]=Node()
                    curr=curr.children[c]
                    print(curr.children)
                curr.isLast=True
               
            
            def search(self,word):
                
                curr=self.root
                for c in word:
                    if c not in curr.children:
                        
                        return False
                    curr=curr.children[c]
                return curr.isLast

        trie=Trie()
        for i in words:
            trie.insert(i)
        
        res=[]
        def dfs(r,c,node,path,word):
            if node.isLast:
                res.append(word)
                node.isLast=False
            if (r<0) or (c<0) or  (r>len(board)-1) or (c >len(board[0])-1) or (r,c) in path or board[r][c] not in node.children:
                return 
            print()
            print("PAth:",path)
            path.add((r,c))
            child=node.children[board[r][c]]
            print("CHild:",child)
            w=word+board[r][c]
            print("WOrd:",w)
            dfs(r+1,c,child,path,w)
            dfs(r-1,c,child,path,w)
            dfs(r,c+1,child,path,w)
            dfs(r,c-1,child,path,w)

            path.remove((r,c))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,trie.root,set(),"")
        return res
                