from collections import defaultdict


strs = ["eat","tea","tan","ate","nat","bat"]

dict=defaultdict(list)
# optimal = O(m*n*26)

for  i in range(len(strs)):
    count=[0]*26
    for j in strs[i]:
        count[ord(j)-ord('a')]+=1
    dict[tuple(count)].append(strs[i])
print(dict.values())
# for i in range(len(strs)):
#     lst=[]
#     for j in range(len(strs[i])):
#         lst.append(strs[i][j])
#     lst.sort()
#     e="".join(lst)
#     if  e not in dict.keys():
#         dict[e]=[strs[i]]
#     else:
#         dict[e].append(strs[i])

# res=[]
# for i in dict.values():
#     res.append(i)
    
    

    # print(strs[i])
# print(res)
    
print(strs,dict)

