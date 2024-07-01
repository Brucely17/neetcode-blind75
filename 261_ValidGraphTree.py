class Node:
    def __init__(self,val):
        self.val=val
        self.neighbor=[]


n=5 
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Input: 
n = 5 
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: false.
graph=set()
for i in range(len(edges)):
    

    node1=Node(edges[i][0])
    node1.neighbor.append(Node(edges[i][1]))
    graph.add(node1)
    node2=Node(edges[i][1])
    
    
        
    count=0
    for node in graph:
        
        print("Nodes:",node.val,node2.val)
        if node.val==node2.val:
            node.neighbor.append(Node(edges[i][0]))
            break
        count+=1
        print(count)
    if count==len(graph):
        node2.neighbor.append(Node(edges[i][0]))
        graph.add(node2)
        
    
        

    
# print(graph)
for i in graph:
    for j in i.neighbor:
        print(i.val,j.val)
visit=set()

def dfs(node,prev):
    if node in visit:
        return False
    visit.add(node)
    prev=node
    for i in node.neighbor:
        if i==prev:
            continue
        dfs(i,prev)
    # return True
for c in graph:
    print(dfs(c,prev=None))