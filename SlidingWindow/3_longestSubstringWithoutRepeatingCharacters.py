class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) ==0:
            return 0
        i=0
        j=1
        string=''
        string+=s[i]
        count=1
        while j<len(s):
            

            if s[j] not in string:
                string+=s[j]
                j+=1

            
            else:
                count=max(count,len(string))
                
                
                i+=1
                string=s[i:j]
                
            
        return max(count,len(string))
        
        


        