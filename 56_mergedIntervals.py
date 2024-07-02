intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
[[1,4],[0,1]]
merge=[]

# for i in range(len(intervals)-1):
#     print(i,merge)
#     if (intervals[i][1]>=intervals[i+1][0]):
#         merge.append([min(intervals[i][0],intervals[i+1][0]),intervals[i+1][1]])
#         intervals[i+1]=merge[-1]
#     else:
#         merge.append(intervals[i])

# print(merge)
intervals.sort(key=lambda x:x[0])
       
        
i=0
while i<len(intervals)-1:
    if (intervals[i][1]>=intervals[i+1][0]):
        if intervals[i+1][1]>=intervals[i][0]:
            
            intervals[i]=[min(intervals[i][0],intervals[i+1][0]),max(intervals[i+1][1],intervals[i][1])]
            intervals.remove(intervals[i+1])
        else:
            intervals[i],intervals[i+1]=intervals[i+1],intervals[i]
    else:
        i+=1
return intervals
        


        