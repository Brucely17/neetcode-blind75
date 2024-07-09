class Solution:
    def countSubstrings(self, s: str) -> int:
        # if s==s[::-1]:
        #     return s
        res=0
        maxsize=0

        

        for i in range(len(s)):

            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                # if maxsize<(r-l+1):
                #     maxsize=r-l+1
                #     res=s[l:r+1]
                res+=1
                l-=1
                r+=1
            # oddEvefun(l,r,res)


            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                # if maxsize<(r-l+1):
                #     maxsize=r-l+1
                #     res=s[l:r+1]
                res+=1
                l-=1
                r+=1
        return res
        