height=[1,8,6,2,5,4,8,3,7]

i=0
j=len(height)-1

maxarea=0


while i<j:
    h=min(height[i],height[j])
    l=j-i
    area=l*h
    maxarea=max(maxarea,area)
    if height[i]>height[j]:
        j-=1
    else:
        i+=1
    print(maxarea)
