# Using Hashmap to solve in O(n) complexity 
# Sum of two elements in array should be target


def twosum(array,target):

    hashmap={}

    for i ,n in enumerate(array):

        difference =  target-n #this is the main concept

        if difference in hashmap:
            return [hashmap[difference],i]
        hashmap[n]=i
    return


print(twosum([2,7,11,15],9))
