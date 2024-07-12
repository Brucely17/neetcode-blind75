# Applying two pointer sollution 


def bestDayToSellStock(array):
    left=0
    right=1

    maxprofit=0

    for i in range(len(array)-1):
        profit=array[right]-array[left]
        print(profit,i,left,right)
        if profit >maxprofit:
            maxprofit=profit
        
        if array[left]>=array[right]:
            left=right
            right+=1
        elif array[right]>array[left]:
            right+=1
    return maxprofit

print(bestDayToSellStock([7,1,5,3,6,4]))
