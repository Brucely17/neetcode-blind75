# Bit manipulation

# a=1
# b=2
# print(a&b)
# print(a^b)

a=2
b=3


# works in java not in python 
while (b!=0):
    tmp = (a&b)<<1
    a=a^b
    b=tmp
print(a)

# python - bit manipulation
class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_int, mask = 0x7FFFFFFF, 0xFFFFFFFF
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        return a if a <= max_int else ~(a ^ mask)

'''

Usage of log also can help and its correct but may not pass test cases

or use SUM in python lib function
'''


