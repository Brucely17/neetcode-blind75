# solve in o(n) without dividing the output

#finindg prefix and postfix values


def productArray(array):
    # Example array [1,2,3,4]

    result=[1]*len(array)

    prefix=1 # as storing prefix value of first value in array to be kept neutral is kept as one 

    for i in range(len(array)):
        result[i]=prefix
        prefix*=array[i]
        #[1,1,2,6]
    print(result)


    postfix=1
    for j in range(len(array)-1 ,-1,-1):
        result[j]*=postfix
        postfix*=array[j]
        # [24,12,4,1]
    print(result)

productArray([1,2,3,4])
# answer [24, 12, 8, 6]

    # for k in range(len())
    

    