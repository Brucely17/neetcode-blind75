nums = [2,3,1,1,4]
cur=nums[0]
for i in range(1,len(nums)):
    if cur==0:
        print("False")
    cur-=1
    cur=max(cur,nums[i])
