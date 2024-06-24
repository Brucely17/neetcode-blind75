text1 = "abcde"
text2 = "ace" 

# 2d DP 

dp=[[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]



for i in range(len(text1)-1,-1,-1):
    for j in range(len(text2)-1,-1,-1):
        if text1[i]==text2[j]:
            dp[i][j]=1+dp[i+1][j+1] #diagonal value
        else:
            dp[i][j]=max(dp[i][j+1],dp[i+1][j]) # taking max of down value or right value
print(dp[0][0])