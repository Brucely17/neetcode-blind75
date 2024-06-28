m=3
n=2
dp=[[0 for i in range(n)] for j in range(m)]
dp[m-1][n-1]=0
dp[m-2][n-1]=1
dp[m-1][n-2]=1



# for i in range(2,n):
#     print(i,i-1,dp[0][i-1])
#     dp[0][i]+=dp[0][i-1]+1
# for k in range(2,m):
#     dp[k][0]+=dp[k-1][0]+1

print(dp)
for i in range(m-1,-1,-1):
    for j in range(n-1,-1,-1):
        if i==m-1 and j==n-1:
            continue
        elif j==n-1:
            dp[i][j]+=dp[i+1][j]
        elif i==m-1:
            dp[i][j]+=dp[i][j+1]
        else:
            dp[i][j]+=dp[i+1][j]+dp[i][j+1]
        for k in dp:
            print(k)
        print("\n")


for i in dp:
    print(i)
        

        

print(dp)