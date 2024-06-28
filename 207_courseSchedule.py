n=5
prerequsite=[[0,1],[0,2],[1,3],[1,4],[3,4]]
# n= 2 
# prerequsite = [[1,0],[0,1]]
# n=3
# prerequsite=[[1,0],[0,2],[2,1]]
class Node:
    def __init__(self,val):
        self.val=val
        self.neighbor=[]
graph=[]
for j in range(n):
    graph.append(Node(j))
for i in prerequsite:
    # print(i)
    # print(graph[i[1]].val,graph[i[0]].val)
    
    graph[i[0]].neighbor.append(graph[i[1]])



for i in graph :
    print(i.neighbor)
visited=set()

def dfs(node):
    print("Node :",node.val)
    if node in visited:
        return False
    if node.neighbor==[]:
        return True
    visited.add(node)
    
    for i in node.neighbor:
        if not dfs(i):
            return False
    visited.remove(node)
    graph[node.val].neighbor=[]
    return True


for i in range(n):
    if not dfs(graph[i]): 
        print( False)
print(True)
        
# print(dfs(graph,graph[0],visited))

