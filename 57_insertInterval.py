intervals = [[1,3],[6,9]]
newInterval = [2,5]


# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newInterval = [4,8]

intervals=[[1,5]]
newInterval=[0,6]


res=[]
for i in range(len(intervals)):
    if newInterval[1]<intervals[i][0]:
        res.append(newInterval)
        return res+intervals[i:]
    elif newInterval[0]>intervals[i][1]:
        res.append(intervals[i])
    else:
        newInterval[0]=min(intervals[i][0],newInterval[0])
        newInterval[1]=max(intervals[i][1],newInterval[1])

res.append(newInterval)
return res

# adding the interval to any available
# for i in range(len(intervals)):
            
#             if intervals[i][0]<newInterval[0] and intervals[i][1]>newInterval[0]:
#                 end=intervals[i][1]
#                 newend=newInterval[1]
#                 maxend=max(end,newend)
#                 intervals[i]=[intervals[i][0],maxend]
#                 break
#             elif intervals[i][0]<=newInterval[1] and intervals[i][1]>newInterval[1]:
#                 intervals[i]=[newInterval[0],intervals[i][1]]
#                 break
#             elif newInterval[0]<intervals[i][0] and newInterval[1]>intervals[i][1]:
#                 intervals[i]=newInterval
#                 break
#             if i>=len(intervals)-1:
#                 intervals.append(newInterval)
#                 intervals.sort(key=lambda x:x[1])
#                 print(intervals)
# i=0
# while i<len(intervals)-1:
#     if intervals[i][1]==intervals[i+1][0]:
#         intervals[i]=[intervals[i][0],intervals[i+1][1]]
#         intervals.remove(intervals[i+1])
#         i-=1
#     elif intervals[i+1][0]<intervals[i][1]:
#         intervals[i]=[intervals[i][0],max(intervals[i][1],intervals[i+1][1])]
#         intervals.remove(intervals[i+1])
#         i-=1
#     i+=1
# print(intervals)