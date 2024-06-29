heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]



ROWS,COLS=len(heights),len(heights[0])

pac,alt = set(),set()

def dfs(r,c,visited,prevHeight):
    if (r<0 or c<0 or (r,c) in visited or r==ROWS or c==COLS or heights[r][c]<prevHeight):
        return 
    visited.add((r,c))
    dfs(r+1,c,visited,heights[r][c])
    dfs(r-1,c,visited,heights[r][c])
    dfs(r,c+1,visited,heights[r][c])
    
    dfs(r,c-1,visited,heights[r][c])

for r in range(ROWS):
    dfs(r,0,pac,heights[r][0])
    dfs(r,COLS-1,alt,heights[r][COLS-1])

for c in range(COLS):
    dfs(0,c,pac,heights[0][c])
    dfs(ROWS-1,c,alt,heights[ROWS-1][c])


res=[]
for r in range(ROWS):
    for c in range(COLS):
        if (r,c) in pac and (r,c) in alt:
            res.append((r,c))
            