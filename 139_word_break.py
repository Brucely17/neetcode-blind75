s = "applepenapple"
wordDict = ["apple","pen"]
s = "leetcode"
wordDict = ["leet","code"]
# s = "catsandog"
# wordDict = ["cats","dog","sand","and","cat"]
# count=0

# s='a'
# wordDict=['b']

# s='a'
# wordDict=['a']
# s='cars'
# wordDict=["car","ca","rs"]

# wordDict.sort()
# current=0
# index=0
# res=s
# for j in range(len(s)):

    
#     for i in wordDict:
         
#         if s[index:index+len(i)]==i:
#             print(index,i)
#             count+=1

#             index+=len(i)-1
#             current=index
            
            
            
#             # print(s[index+len(i)])
#             break
#         if index>=len(s)-1:
#             break
        
#     if index>=len(s)-1:
#             break  
#     index+=1  
#     res=s[index:]
# print(wordDict,count,index,current)
# print(res)



# # for j in range(len(s)):

    
# #     for i in wordDict:
# #         if j>=len(s)-1:
# #             break 
# #         if s[j:j+len(i)]==i:
# #             print(j,i)
# #             count+=1
# #             index=j+len(i)
            
            
# #             print(s[j:j+len(i)])
# #             break
        
# #     if j==len(s)-1:
# #             break    
# # print(wordDict,count,index)
dp = [False] * (len(s) + 1)
dp[0] = True

# Iterate through the string
for j in range(len(s) + 1):
    for word in wordDict:
        if j >= len(word) and s[j-len(word):j] == word:
            dp[j] = dp[j] or dp[j-len(word)]
            print(dp, s[j-len(word):j])
        if dp[j]:
            break


