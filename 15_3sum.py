nums = [-1,0,1,2,-1,-4]
# nums = [0,1,1]
nums = [0,0,0,0]
nums=[-1,0,1,2,-1,-4,-2,-3,3,0,4]

array=[]
nums.sort()
# print(nums)


for i in range(len(nums)):
    a=nums[i]
    if i>0 and a==nums[i-1]:
        continue

    l,r=i+1,len(nums)-1
    while l<r:
        sum= a + nums[l]+nums[r]
        if sum==0:
            print(a,nums[l],nums[r])
            # res=[a,nums[l],nums[r]]
            # if res not  in array:
            array.append([a,nums[l],nums[r]])
            l+=1
            while nums[l]==nums[l-1] and l<r:
                l+=1

        elif sum>0 :
            r-=1
        else:
            l+=1

       

    
# print(nums[l+1:r],nums[:r])
# while l<r:

#     sum=nums[l]+nums[r]
#     for i in range(len(nums)-1):
#         if i >0 and nums[i]==nums[i-1] :
#             continue


#         if nums[i] in nums[l+1:r]:
#             print(nums[l],nums[r],nums[i])
#             res=[nums[l],nums[r],-sum]
#             if res not  in array:
#                 array.append([nums[l],nums[r],-sum])
#     if abs(nums[l])>abs(nums[r]):
#         l+=1
#     else:
#         r-=1
    
print(array)
