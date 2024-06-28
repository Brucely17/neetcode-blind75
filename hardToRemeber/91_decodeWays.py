s = "226"
# s='11106'
# s='06'
# s='12'
# s='1123'
nums=[]
for i in s:
    if i=='0':
        if len(nums)!=0:
            nums[-1]+=i
    else:
        nums.append(i)
print(nums)
dp=[0 for i in range(len(nums)+1)]
# print(dp)
dp[-1]=1

for i in range(len(nums)-1,-1,-1):
   
    if int(nums[i])<=26:
        dp[i]=dp[i+1]
        if i + 1 < len(nums) and int(nums[i]+nums[i+1])<=26:
            dp[i]+=dp[i+2]
            print(dp)
        

    
        
print(dp)
