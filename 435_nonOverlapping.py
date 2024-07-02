intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1,2],[1,2],[1,2]]
intervals = [[1,2],[2,3]]
intervals=[[1,100],[11,22],[1,11],[2,12]]
intervals.sort(key=lambda x:x[0])
print(intervals)
        
i=0
count=0
while i<len(intervals)-1:
    if (intervals[i][1]>intervals[i+1][0]):
        if intervals[i+1][1]>intervals[i][0]:
            
            # intervals[i]=[min(intervals[i][0],intervals[i+1][0]),max(intervals[i+1][1],intervals[i][1])]
            if intervals[i+1][1]>intervals[i][1]:
                intervals.remove(intervals[i+1])
            else:
                intervals.remove(intervals[i])
                
            count+=1
        elif intervals[i+1][1]<intervals[i][0]:
            intervals[i],intervals[i+1]=intervals[i+1],intervals[i]
    else:
        i+=1
print(count,intervals)