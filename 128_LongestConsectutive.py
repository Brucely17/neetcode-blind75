nums = [100,4,200,1,3,2]
s=sum(nums)
print(s)
nums = [0,3,7,2,5,8,4,6,0,1]
# nums=set(nums)

nums=set(nums)
print(nums)


maxcount=0
for i in nums:
    
    if i+1 in nums :
        temp=i
        
        count=1
        while temp+1 in nums:
            
            temp+=1
           
            count+=1
        maxcount=max(maxcount,count)
    if maxcount>len(nums)//2:
        break
print(maxcount)
