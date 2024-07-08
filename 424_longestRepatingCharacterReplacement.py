s = "AABABBA"
k = 1
s = "ABAB"
k = 2

i=0
j=0

count={}
res=0
maxf=0
for j in range(len(s)):
    count[s[j]]=1+count.get(s[j],0)
    maxf=max(count[s[j]],maxf)

    while (j-i+1)-maxf >k:
        count[s[i]]-=1
        i+=1
    res=max(res,j-i+1)
print(res)
    
