'''
nums of money in each house is given

constraint - should not jump to adjacent num in list
'''

nums = [2,7,9,3,1]

dp=[0 for i in range(len(nums))]
print(dp)
dp[-1]=nums[-1]
dp[-2]=nums[-2]

for i in range(len(nums)-3,-1,-1):
    maxim=dp[i-2]
    for j in range(i+2,len(nums)):
        print(i,nums[i],j)
        maxim=max(maxim,dp[j]+nums[i])
        dp[i]=maxim
    print(dp)

        
    