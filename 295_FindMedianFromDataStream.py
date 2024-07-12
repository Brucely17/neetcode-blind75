class MedianFinder:

    def __init__(self):
        # two heaps - large ,small ,minheap ,maxheap 
        # heaps should be equal size
        self.small=[]
        self.large=[]
        

    def addNum(self, num: int) -> None:
        # As python provides only min heap we multiply by negative 

        # Every num in small heap <= every num in large 
        heapq.heappush(self.small,-1*num)

        if (self.small and self.large and (-1* self.small[0])>self.large[0]):
            val=heapq.heappop(self.small)*-1
            heapq.heappush(self.large,val)
        
        # isze should not be uneveen mshould equal or only one grater than other 
        if len(self.small) > len(self.large) +1 :
            val=-1* heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if len(self.small)+1 < len(self.large)  :
            val=heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)

        

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        if len(self.large)>len(self.small):
            return self.large[0]
        
        return (-1*self.small[0]+self.large[0])/2
        
