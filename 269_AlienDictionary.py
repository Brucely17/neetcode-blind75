# Hard Problem - Toploogical Sort 
'''

ex:[wrt,wrf]

we check for sorting :
w,w same
r ,r same
t,f differs ,so in alien language: t is first then f=>[t,f]

[apes,ape]
as s in only remaining and here nothis is there so we cant sort according to question ,its return ""




Think like automata language drawing graph

doing postorder DFS and reversing reuslt =>Topological sort 
 


'''
words=["wrt","wrf","er","ett","rftt"]
# output "wertf"


adj={c:set() for w in words for c in w}

for i in range(len(words)-1):
    w1,w2=words[i],words[i+1]
    minLen=min(len(w1),len(w2))

    if len(w1)>len(w2) and w1[:minLen] ==w2[:minLen]:
        # return ""
        print("")
    for j in range(minLen):
        if w1[j]!=w2[j]:
            adj[w1[j]].add(w2[j])
            break

visit={}
res=[]

def dfs(c):
    if c in visit:
        return visit[c]
    visit[c]=True
    for nei in adj[c]:
        if dfs(nei):
            return True
    visit[c]=False
    res.append(c)
    # reverse adding

for c in adj:
    if dfs(c):
        # return ""
        print("")
        break

print("".join(res[::-1]))
