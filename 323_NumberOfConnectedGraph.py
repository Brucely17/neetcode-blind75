'''
Leetcode premium 

UnionFind algoithm => ADSA = Kruskals algorithm 
'''
n=5
edges = [[0, 1], [1, 2], [3,4]]
parent=[i for i in range(n)]


rank=[1]*n

def find (n1):
    res=n1

    while res!=parent[res]:
        parent[res]=parent[parent[res]] #path compression
        res=parent[res]
    print(res)
    return res

def union(n1,n2):
    p1,p2=find(n1),find(n2)


    if p1==p2 :
        return 0 
    if rank[p2]> rank[p1]:
        parent[p1]=p2
        rank[p2]+=rank[p1]
    else:
        parent[p2]=p1
        rank[p1]+=rank[p2]
    return 1

res=n

for n1,n2 in edges :
    res-=union(n1,n2)
print(res)




isConnected = [[1,1,0],[1,1,0],[0,0,1]]

edges=[]

for i in range(len(isConnected)):
    new=[]
    for j in range(len(isConnected[0])):
        if isConnected[i][j]==1:
            new.append(j)
    if new is not None and sorted(new) not in edges:
        edges.append(new)
print(edges)