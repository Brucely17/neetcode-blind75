board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"

path=set()
def dfs(r,c,count):
    if (r<0 or c<0 or r>len(board)-1 or c>len(board[0])-1 or word[count]!=board[r][c] or (r,c) in path):
        return False
    if count==len(word):
        return True
    path.add((r,c))
    res=dfs(r+1,c,count+1) or dfs(r-1,c,count+1) or  dfs(r,c+1,count+1) or dfs(r,c-1,count+1)
    path.remove((r,c))
    return res
for i in range(len(board)):
    for j in range(len(board[0])):
        if dfs(i,j,0):
            print(True)
print(False)

# def recSearch(letter,i,j,str,count,visited):
#     print(letter,word,i,j,count)
    
#     if i-1>=0:
#         if board[i-1][j]==letter and [i-1,j] not in visited:
#             print('\nCOndition1:')
#             print(word,i,j,count,str,visited)
#             visited.append([i-1,j])
#             if str==word[1:]:
#                 print(True)
#                 return True
#             else:
#                 recSearch(word[count+1],i-1,j,str+word[count+1],count+1,visited)
#     if j-1>=0:
#         if board[i][j-1]==letter and [i,j-1] not in visited:
#             print('\nCOndition2:')
            
#             print(word,i,j,count,str,visited)
#             visited.append([i,j-1])
#             if str==word[1:]:
#                 print(True)
#                 return True
#             else:
            
#                 recSearch(word[count+1],i,j-1,str+word[count+1],count+1,visited)
    
#     if i+1<len(board):
#         if board[i+1][j]==letter and [i+1,j] not in visited:
#             print('\nCOndition3:')
#             # print(word,i,j,count)
#             print(word,i,j,count,str,visited)
#             visited.append([i+1,j])
#             if str==word[1:]:
#                 print(True)
#                 return True
#             else:
#                 recSearch(word[count+1],i+1,j,str+word[count+1],count+1,visited)
    
#     if j+1<len(board[0]):
#         if board[i][j+1]==letter and [i,j+1] not in visited:
#             print('\nCOndition4:')
#             # print(word,i,j,count)
#             print(word,i,j,count,str,visited)
#             visited.append([i,j+1])
#             if str==word[1:]:
#                 print(True)
#                 return True
#             # print(str[0],str[count+1:])
#             else:
#                 recSearch(word[count+1],i,j+1,str+word[count+1],count+1,visited)
   

#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j]==word[0]:
#                 visited=[]
#                 visited.append([i,j])
#                 if recSearch(word[1],i,j,word[1],1,visited):
#                     print("True")
#                     return True
                
# # exist()
        
