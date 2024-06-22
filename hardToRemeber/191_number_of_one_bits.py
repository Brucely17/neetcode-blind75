
# simple method 
# shifting the bit right side one by one
# checking with mod 2,if its 0 ,it returns 0 ,while if  ,it returns 1

n=00000101
res=0

while n:
    res+=n%2
    n=n>>1
    print(res)
print(res)


'''
Most effectve way : using and 
ex:10001
n=n&(n-1)
subtracting : n-1= 10000
then and = 10000, now after this one operation we increment res+=1

again,sub=01111
then and= 000000,now we get all zero and res=2,this is how it works
'''

res=0
while n:


    n=n&(n-1)
    res+=1

print(res)
    
    