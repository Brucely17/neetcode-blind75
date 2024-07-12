s = "cbbd"
s = "babad"
s.isn

''' DP solution '''
dp=[[i] for i in s]
count=0
res=''
# count=0
print(dp)
for i in range(len(s)-2,-1,-1):
    print(s[i],dp[i],dp[i+1])
    # dp[i].append(dp[i+1][0])
    for j in dp[i+1]:
        val=dp[i][0]+j
        if count<len(val):
            if val==val[::-1]:
                # if count<len(val):
                res=val
                count=len(val)
            dp[i].append(val)
    # print(dp[i])
    


# print(dp)
for i in dp:
    print(i)
print(res)

'''eficient Solution '''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if len(s)<=1:
        #     return s
        if s==s[::-1]:
            return s
        res=''
        maxsize=0

        # def oddEvefun(l,r,res):
        #     while l>=0 and r<len(s) and s[l]==s[r]:
        #         if maxsize<(r-l+1):
        #             maxsize=r-l+1
        #             res=s[l:r+1]
        #         l-=1
        #         r+=1


        for i in range(len(s)):

            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if maxsize<(r-l+1):
                    maxsize=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
            # oddEvefun(l,r,res)


            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if maxsize<(r-l+1):
                    maxsize=r-l+1
                    res=s[l:r+1]
                l-=1
                r+=1
        return res