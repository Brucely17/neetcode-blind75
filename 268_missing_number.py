nums=[3,0,1]
# n=3
# ans=2

if len((nums)) not in nums:
    print(len(nums))
for i in range(len(nums)):
    if i not in nums:
        print(i)
        break

# XOR solution 
res=len(nums)

for i in range(len(nums)):
    res^=i^nums[i]

print(res)

