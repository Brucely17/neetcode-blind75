from math import inf


s = "ADOBECODEBANC"
t = "ABC"

countT={}
for c in t:
    countT[c]=1 + countT.get(c,0)
window={}

have=0
need=len(t)

res=[-1,-1]
resLen=float(inf)
l=0
r=0

for r in range(len(s)):
    c=s[r]
    window[c]=1+window.get(c,0)

    if c in countT and window[c]==countT[c]:
        have+=1
    
    while have ==need:
        if resLen>r-l+1:
            res=[l,r]
            resLen=r-l+1
        window[s[l]]-=1
        if s[l] in countT and window[s[l]]<countT[s[l]]:
            have-=1
        l+=1
if resLen!=float(inf):
    print(res)
else:
    print('')


# temp=[]
# for i in range(len(t)):
#     temp.append(t[i])


# i=0
# j=0
# count=0
# size=float(inf)
# ptr=i
# while j<len(s)-1:
#     print("\nregular:",i,j, s[i],temp,s[j],size,ptr)
#     if s[j] in temp:
#         temp.remove(s[j])

#         count+=1
#         if count==2:
#             ptr=j
#         j+=1
#         print("\nCondirion1:")
#         # print(i,j, s[i],temp,s[j],size)
#     elif s[j] not in temp and s[j] not in t :
#         j+=1

#     elif s[j] not in temp and s[j] in t:
#         i=ptr
#         count=0
#         j=i 
#         temp=[]
#         for x in range(len(t)):
#             temp.append(t[x])
#         print("\n Condition2:")
#         print(i,j, s[i],temp,s[j],size)
    
    
#     if len(temp)==0:
#         size=min(size,j-i) 
#         print("Result:",s[i:j])
#         count=0
#         i=ptr
#         j=i
#         temp=[]
#         for x in range(len(t)):
#             temp.append(t[x])
#         print('condition3:')
#         print(i,j, s[i],temp,s[j],size)
# print(s[i:j])
#     # j+=1
#     # break