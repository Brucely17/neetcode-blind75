# ALgo in o(log n) 

nums=[3,4,5,1,2]


'''
we are going to use binary search

first mark the middle element ,set min value=mid
then to find whether we have to search in lft sub array or right sub array ,
we compare if nums[mid]<nums[0] ,then search right
else search left 


'''
# nums = [4,5,6,7,0,1,2]
# nums = [11,13,15,17]
# mid =len(nums)/2
# if len(nums)%2==0:
#     mid =len(nums)/2
# else:
#     mid =(len(nums)+1)/2

# minim=nums[int(mid)-1]
def findMin(nums,minim):
    
    if len(nums)%2==0:
        mid =len(nums)/2
    else:
        mid =(len(nums)+1)/2
    if mid>len(nums)-1:
        return minim
    minim=min(minim,nums[int(mid)-1])
    # print(minim,nums[int(mid)-1])
    if nums[int(mid)-1]>nums[0]:
        
        print(nums[int(mid)-1:])
        return findMin(nums[int(mid)-1:],minim)
    else:
        print(nums[:int(mid)])
        return findMin(nums[:int(mid)],minim)
    

print(findMin(nums,nums[0]))


    
