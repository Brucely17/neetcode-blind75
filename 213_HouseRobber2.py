nums=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
output=16

''''
Reusing hpuse robber 1 solution with including of below last index one case
other case above first index
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==2:
            return max(nums[0],nums[1])
        elif len(nums)==1:
            return nums[0]
        def houseRob(nums):
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
            return max(dp)


        print(houseRob(nums[:len(nums)-1]))
        print(houseRob(nums[1:]))
        return max(houseRob(nums[:len(nums)-1]),houseRob(nums[1:]))
        

