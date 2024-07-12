board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

def exist(board, word: str) -> bool:
    ROW=len(board)
    COL=len(board[0])
    path=set()
    def dfs(r,c,count):
        if count==len(word):
            return True
        if (r<0 or c<0 or r>=ROW or c>=COL or word[count]!=board[r][c] or (r,c) in path):
            return False
        
        path.add((r,c))
        res=dfs(r+1,c,count+1) or dfs(r-1,c,count+1) or  dfs(r,c+1,count+1) or dfs(r,c-1,count+1)
        path.remove((r,c))
        return res
    for i in range(ROW):
        for j in range(COL):
            if dfs(i,j,0):
                # print(True)
                return True
    # print(False)
    return False
print(exist(board,word))