# Solving using DP

# In product we care about negative value and 0

nums = [2,3,-2,4]
# nums=[-2,0,-1]


result=max(nums) #cover cases where array may containe only -ve numbers
currMax,currMin=1,1 #maximum and minimum value ending at current element

for n in nums:

    temp=currMax*n
    currMax=max(n,currMax*n,currMin*n)
    '''
    currMin * n: The product of the current number and
    the previous minimum product. This is crucial because
      a negative number times the previous minimum product 
    (which could be negative) might yield a large positive product.
    '''
    currMin=min(n,temp,currMin*n)

    result=max(result,currMax)
print(result) 

            

        

