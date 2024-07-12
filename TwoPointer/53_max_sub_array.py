# Input: [-2,1,-3,4,-1,2,1,-5,4]

# the concept is to eliminte subbarays ,which doesnot contribute anything

'''
Lets look it this way
first -2 ,maxsum=-2,len=1
second -2 +1=-1 ,as maxsum <next number 1,eliminate the before value completely,
second 1 ,maxsum=1,len=1
third -2 ,maxsum<third,len=2,also eleminiate 

third -3 + 4 <4 ,so eleimiate

4 th 4,maxsum=4,len=1
fifth 3 ,maxsum=4 ,len=2
sixth 5 ,maxsum=5 ,len=3
seventh 6 ,maxsum=6,len=4 ,after this if we compute it would give less result n computation ,
but this is how the idea works
'''


def maxSumArray(nums):

    maxsum=nums[0]
    maxlen=1
    final=maxsum
    for i in range(1,len(nums)):
        
        sum=maxsum+nums[i]


        if final<sum:
            final=sum
        


        if nums[i]>maxsum:
            maxsum=nums[i]
            maxlen=1
        else:
            maxsum=sum
            maxlen+=1
        
        print(nums[i],maxsum,final)
    return final
print(maxSumArray([-2,1,-3,4,-1,2,1,-5,4]))