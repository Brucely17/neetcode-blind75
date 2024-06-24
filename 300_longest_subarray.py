# dynamic programming


nums = [10,9,2,5,3,7,101,18]
nums = [0,1,0,3,2,3]
# nums = [7,7,7,7,7,7,7]
# nums=[4,10,4,3,8,9]

'''
ex:[1,2,4,3]

lIs[3]=1
lis[2]=1
lis[1]=2
lis[0]=3
backward dynamic programming
'''



dp=[1]*(len(nums))

for i in range(len(nums)-1,-1,-1):
    for j in range(i+1,len(nums)):
        if nums[i]<nums[j]:
            dp[i]=max(dp[i],1+dp[j])

print(dp)