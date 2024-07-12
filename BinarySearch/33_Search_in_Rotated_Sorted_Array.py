# solve for O(logn)
nums = [4,5,6,7,0,1,2]
# nums = [1]
# nums=[5,1,3]


l,r=0,len(nums)-1
target=2
while l<=r:
    mid=(l+r)//2

    if nums[mid]==target:
        print(mid)
    
    # left sorted array 
    if nums[l]<=nums[mid]:
        if target >nums[mid] or target <nums[l]:
            l=mid+1
        else:
            r=mid-1
    
    # right sorted array 
    else:
        if target <nums[mid] or target >nums[r]:
            r=mid-1
        else:
            l=mid+1
        



